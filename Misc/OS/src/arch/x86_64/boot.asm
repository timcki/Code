global start        ; makes it global, public. entry point of the kernel so needs to be callable.
extern long_mode_start

section .text       ; default section for executable code
bits 32             ; specifies 32-bit instructions. The processor is still in protected mode.
start:
        mov esp, stack_top

        ; Doing ale the checks for booting into long mode
        call check_multiboot
        call check_cpuid
        call check_long_mode

        call set_up_page_tables
        call enable_paging

        ; Load Global Descriptor Table
        lgdt [gdt64.pointer]

        ; Performing a long jump
        jmp gdt64.code:long_mode_start

        mov dword [0xb8000], 0x2f4b2f4f    ; print OK to screen. Moves to VGA buffer (?)
        hlt                                 ; stop execution

error:
        mov dword [0xb8000], 0x4f524f45
        mov dword [0xb8004], 0x4f3a4f52
        mov dword [0xb8008], 0x4f204f20
        mov byte  [0xb800a], al
        hlt

; Reserve place for the stack. GRUB takes care of that while initiazling

; Checks if multiboot is enabled. Bootloader should push a cookie value to eax. It not there give error code zero and jmp to error
check_multiboot:
        cmp eax, 0x36d76289
        jne .nomultiboot
        ret
.nomultiboot:
        mov al, "0"
        jmp error       ; We use jmp instead of call  here because we dfc. It'd push the return address to the stack but why bother if error doesn't return.

; CPUID is a processor instruction to get info about itself
check_cpuid:
        ;check if cpuid is supported by attempting to flip it ID bit (21 bit) in FLAGS
        pushfd
        pop eax
        ;copy to ecx to comparing later on
        mov ecx, eax
        ;flip bit
        xor eax, 1 << 21
        ;same as before but now using stack to copy from eax to flags
        push eax
        popfd
        pushfd
        pop eax

        push ecx
        popfd

        cmp eax, ecx
        je .no_cpuid
        ret
.no_cpuid:
        mov al, "1"
        jmp error

; Checking if long mode is supported
check_long_mode:
        mov eax, 0x80000000    ; argument for cpuid
        cpuid                   ; get highest supported value
        cmp eax, 0x80000001     ; needs to be at least 80000001
        jb .no_long_mode

        mov eax, 0x80000001
        cpuid
        test edx, 1 << 29
        jz .no_long_mode
        ret
.no_long_mode:
        mov al, "2"
        jmp error
        
set_up_page_tables:
        mov eax, p3_table
        or eax, 0b11        ; Present + writable
        mov [p4_table], eax

        mov eax, p2_table
        or eax, 0b11
        mov [p3_table], eax

        mov ecx, 0
; We need to set up every P2 entry to point to a subsequent 2MiB page so we sue and assembly loop. ecx is the counter and we increment 512 times to set up 1 GiB of paged
; memory
.map_p2_tables:
        mov eax, 0x200000   ;2MiB
        mul ecx             ; start page of exc-th page (first 0, then 2MiB, then 4MiB etc...)
        or eax, 0b10000011  ; set up present, writable and HUGE bits on each page
        mov [p2_table + ecx * 8], eax ; Basically what we're doing is indexing the page with the value of eax. So setting the bits that you see in the command above

        inc ecx
        cmp ecx, 512        ; 2MiB * 512 == 1 GiB of memory
        jne .map_p2_tables  ; if less jmp to beginning of subroutine

        ret

enable_paging:
        ; Load first address of P4 table to cr3 register. The processor looks there default for paging.
        ; Obviously you can't load directly to cr3 so we use eax as a buffer to do that
        mov eax, p4_table
        mov cr3, eax
        
        ; Enable PAE-flag in cr4, which is the (Physcial Address Extension). Again eax is the buffer cause we can't write to cr4 directly
        mov eax, cr4
        or eax, 1 << 5
        mov cr4, eax

        ; Set the long mode bit in the EFER MSR (Model Specific Register)
        mov ecx, 0xC0000080
        rdmsr           ; read msr to eax i guess
        or eax, 1 << 8  ; flip bit
        wrmsr           ; write back from eax i guess

        ; Enable paging in the cr0 register
        mov eax, cr0
        or eax, 1 << 31
        mov cr0, eax

        ret


section .bss
align 4096
p4_table:
        resb 4096
p3_table:
        resb 4096
p2_table:
        resb 4096
stack_bottom:
        resb 64
stack_top:

section .rodata
gdt64:
        dq 0    ; zero entry in GDT ( Global Descriptor Table )
.code: equ $ - gdt64
        ; set bits to coresponding values describing desired behavior ( ex. 43 - executable, 44 - descriptor for code and data segments )
        dq (1<<43) | (1<<44) | (1<<47) | (1<<53)
.pointer:
        dw $ - gdt64 - 1    ; dollar represents current address so - .pointer
        dq gdt64
