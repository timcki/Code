global long_mode_start

section .text
bits 64
long_mode_start:
        mov rax, 0x2f592f412f4b2f4f ; OKAY
        mov qword [0xb0000], rax
        hlt
