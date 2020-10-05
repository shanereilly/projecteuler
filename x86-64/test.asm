SECTION .DATA
    int_to_str:     db '0123456789'

SECTION .TEXT
    global strlen
    global itostr

    ;RDI, RSI, RDX, RCX, R8, R9, 
    ; Converts integer to string
    ; void itostr(int i, char *buf)
    itostr:
        push    rbp
        mov     rbp, rsp
        mov     r8, 0xa
        mov     rdi, rax
        test    rax, rax    
        jns     .itostr_loop
        neg     rax
        mov     byte [rsi], '-'
        inc     rsi
    .itostr_loop:
        test    rax, rax
        jz      .itostr_done
        xor     rdx, rdx
        div     r8
        lea     rdi, [int_to_str+rdx]
        mov     dil, byte [rdi]
        mov     byte [rsi], dil
        inc     rsi
        jmp     .itostr_loop
    .itostr_done:
        mov     byte [rsi], 0x0             ;add null byte to string
        pop     rbp
        ret

    ; Count number of chars in string (excluding NUL)
    ; size_t strlen(char *str)
    strlen:
        push    rbp
        mov     rbp, rsp
        xor     rcx, rcx    ; zero counter
    .strlen_loop:
        mov     al, byte [rdi]
        test    al, al
        jz      .strlen_done
        inc     rcx
        inc     rdi
        jmp     .strlen_loop
    .strlen_done:
        mov     rax, rcx
        pop     rbp
        ret
    ;_start:
    
