.text
.global _start
_start:

    @ Linha 1
    LDR r0, =C_1
    VLDR d0, [r0]
    LDR r0, =C_2
    VLDR d1, [r0]
    VADD.F64 d0, d0, d1
    LDR r0, =RES_LINHA_1
    VSTR d0, [r0]

    @ Linha 2
    @ RES invalido, carregando 0.0
    LDR r0, =C_3
    VLDR d0, [r0]
    LDR r0, =RES_LINHA_2
    VSTR d0, [r0]

    @ Linha 3
    LDR r0, =C_4
    VLDR d0, [r0]
    LDR r0, =CONTADOR
    VSTR d0, [r0]
    LDR r0, =RES_LINHA_3
    VSTR d0, [r0]

    @ Linha 4
    LDR r0, =MEM
    VLDR d0, [r0]
    LDR r0, =RES_LINHA_4
    VSTR d0, [r0]

    @ Linha 5
    LDR r0, =C_2
    VLDR d0, [r0]
    LDR r0, =C_5
    VLDR d1, [r0]
    VADD.F64 d0, d0, d1
    LDR r0, =C_6
    VLDR d2, [r0]
    LDR r0, =C_7
    VLDR d3, [r0]
    VMUL.F64 d2, d2, d3
    VDIV.F64 d0, d0, d2
    LDR r0, =RES_LINHA_5
    VSTR d0, [r0]

fim:
    B fim

.align 3
C_1: .double 3.14
C_2: .double 2.0
C_3: .double 0.0
C_4: .double 10.5
C_5: .double 3.0
C_6: .double 4.0
C_7: .double 5.0

.data
.align 3
RES_LINHA_1: .double 0.0
RES_LINHA_2: .double 0.0
RES_LINHA_3: .double 0.0
RES_LINHA_4: .double 0.0
RES_LINHA_5: .double 0.0
CONTADOR: .double 0.0
MEM: .double 0.0