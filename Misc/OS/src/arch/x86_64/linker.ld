ENTRY(start)    /* Bootloader with jump here after loading the kernel */

SECTIONS {
        /* Load address of first section at i MiB. Conventional place to load kernel. */
        . = 1M;

        /* Creating to sections in the ELF executable. */
        .boot : {
                /* Ensure that multiboot header is at the beginning */
                *(.multiboot_header)
        }

        /* Contains all sections named text */
        .text : {
                *(.text)
        }
}
