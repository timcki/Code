global start
extern long_mode_start

section .text
bits 32
start:
    mov esp, stack_top

    ; call tests 
    call check_multiboot
    call check_cpuid
    call check_long_mode

    ; paging setup
    call set_up_page_tables
    call enable_paging

    ; load the 64-bit GDT (global descriptor table-relict from segmentation days)
    lgdt [gdt64.pointer]

    ;perform a long jump
    jmp gdt64.code:long_mode_start

    hlt

error:
    mov dword [0xb8000], 0x4f524f45
    mov dword [0xb8004], 0x4f3a3f52
    mov dword [0xb8008], 0x4f204f20
    mov byte  [0xb800a], al
    hlt


check_multiboot:
    cmp eax, 0x36d76289
    jne .no_multiboot
    ret
.no_multiboot:
    mov al, "0"
    jmp error


check_cpuid:
    pushfd              ; Store the FLAGS register
    pop eax             ; Restore eax
    mov ecx, eax        ; mov eax to ecx
    xor eax, 1 << 21    ; Flip 21 bit, ID-bit
    push eax            ; Push eax to the stack
    popfd               ; Restore the FLAGS register
    pushfd              ; Same as before
    pop eax             ; Restore eax to previous state
    push ecx            ; Store ecx
    popfd               ; Restore the FLAGS register
    xor eax, ecx        ; xor eax, ecx
    jz .no_cpuid        ; if they are equal xor will zero them out so it'll error
    ret
.no_cpuid:
    mov al, "1"         ; exit with eroor code one
    jmp error


check_long_mode:
    mov eax, 0x80000000 ; set eax to a lot
    cpuid               ; identify cpu by pushing into eax
    cmp eax, 0x80000001 ; which we compare here
    jb .no_long_mode    ; if less than jump

    mov eax, 0x80000001 ; set eax to a lot + 1
    cpuid
    test edx, 1 << 29   ; test if the 29-th bit is set in edx
    jz .no_long_mode    ; if zero than jump to err code
    ret
.no_long_mode:
    mov al, "2"
    jmp error


set_up_SSE:
    mov eax, 0x1
    cpuid
    test edx, 1<<25
    jz .no_SSE

    mov eax, cr0
    and ax, 0xFFFB
    or ax, 0x2
    mov cr0, eax
    mov eax, cr4
    or ax, 3 << 9
    mov cr4, eax

    ret
.no_SSE:
    mov al, "4"
    jmp error


set_up_page_tables:
    ; map p4 to p3
    mov eax, p3_table
    or eax, 0b11
    mov [p4_table], eax

    ; map p3 to p2
    mov eax, p2_table
    or eax, 0b11
    mov [p3_table], eax

    mov ecx, 0
    
.map_p2_table:
    mov eax, 0x200000
    mul ecx
    or eax, 0b10000011
    mov [p2_table + ecx * 8], eax

    ; for loop
    inc ecx
    cmp ecx, 512
    jne .map_p2_table

    ret


enable_paging:
    ; load p4 to cr3 ( cr3 is used by the cpu to access the table)
    mov eax, p4_table
    mov cr3, eax

    ; enable PAE-flag ( physical address extension ) in cr4
    mov eax, cr4
    or eax, 1 << 5
    mov cr4, eax

    ; set the long mode bit in the EFER MSR ( model specific register )
    mov ecx, 0xC0000080
    rdmsr
    or eax, 1 << 8
    wrmsr

    ; enable paging in the cr0 register
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
    dq 0 ; zero entry
.code: equ $ - gdt64
    dq (1<<43) | (1<<44) | (1<<47) | (1<<53)
.pointer:
    dw $ - gdt64 - 1
    dq gdt64
