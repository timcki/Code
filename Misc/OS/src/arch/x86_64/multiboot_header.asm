section .multiboot_header
header_start:
        dd 0xe85250d6                   ; magic cookie number for it to even boot
        dd 0                            ; number related to architecture of the processor i386 - 0, MIPS - 4
        dd header_end - header_start    ; length of the header
        ; checksum -( cookie + arch number + (header_length) )
        dd 0x100000000 - (0xe85250d6 + 0 + (header_end - header_start))

        ; optional tags (?)

        ; requiered end tag
        ; dw - u16 , dd - u32
        dw 0    ; type
        dw 0    ; flag
        dd 8    ; size
header_end:
