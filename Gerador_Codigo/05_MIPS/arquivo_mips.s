		.text
		.globl main
main:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		li $v1, 4
		move $t0, $v1
		li $v1, 1
		move $t1, $v1
		li $v1, 2
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		mul $v1, $t0, $t1
		move $t0, $v1
		move $a0, $t0
		jal _halloc
		move $t0, $v0
		li $v1, 4
		move $t1, $v1
		li $v1, 6
		move $t2, $v1
		mul $v1, $t1, $t2
		move $t1, $v1
		move $a0, $t1
		jal _halloc
		move $t1, $v0
		move $t2, $t0
		move $t3, $t1
		sw $t3, 0($t2)
		move $t2, $t1
		la $v1, BS_Search
		move $t3, $v1
		sw $t3, 0($t2)
		move $t2, $t1
		la $v1, BS_Compare
		move $t3, $v1
		sw $t3, 4($t2)
		move $t2, $t1
		la $v1, BS_Start
		move $t3, $v1
		sw $t3, 8($t2)
		move $t2, $t1
		la $v1, BS_Init
		move $t3, $v1
		sw $t3, 12($t2)
		move $t2, $t1
		la $v1, BS_Div
		move $t3, $v1
		sw $t3, 16($t2)
		la $v1, BS_Print
		move $t2, $v1
		sw $t2, 20($t1)
		move $t1, $t0
		li $v1, 0
		move $t2, $v1
		sw $t2, 4($t1)
		move $t1, $t0
		li $v1, 0
		move $t2, $v1
		sw $t2, 8($t1)
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L0_MAIN
L0_MAIN:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 8($t1)
		li $v1, 20
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		move $a0, $t0
		jal _print
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl BS_Start
BS_Start:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 12
		sw $s0, -12($fp)
		move $s0, $a0
		move $t0, $a1
		li $v1, 0
		move $t1, $v1
		li $v1, 0
		move $t1, $v1
		move $t1, $s0
		move $t2, $t1
		li $v1, 1
		move $t3, $v1
		slt $v1, $t2, $t3
		move $t2, $v1
		beqz $t2, L1_BS_Start
L1_BS_Start:		nop
		move $t2, $t1
		lw $t2, 0($t2)
		lw $t2, 12($t2)
		move $a0, $t1
		move $a1, $t0
		jalr $t2
		move $t0, $v0
		move $t1, $t0
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L2_BS_Start
L2_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 20($t1)
		move $a0, $t0
		jalr $t1
		move $t0, $v0
		move $t1, $t0
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L3_BS_Start
L3_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 8
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L4_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L5_BS_Start
L4_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L5_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L6_BS_Start
L6_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 19
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L7_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L8_BS_Start
L7_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L8_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L9_BS_Start
L9_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 20
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L10_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L11_BS_Start
L10_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L11_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L12_BS_Start
L12_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 21
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L13_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L14_BS_Start
L13_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L14_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L15_BS_Start
L15_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 37
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L16_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L17_BS_Start
L16_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L17_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L18_BS_Start
L18_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 38
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L19_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L20_BS_Start
L19_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L20_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L21_BS_Start
L21_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 39
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L22_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L23_BS_Start
L22_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L23_BS_Start:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L24_BS_Start
L24_BS_Start:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 0($t1)
		li $v1, 50
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		beqz $t0, L25_BS_Start
		li $v1, 1
		move $t0, $v1
		move $a0, $t0
		jal _print
		b L26_BS_Start
L25_BS_Start:		nop
		li $v1, 0
		move $t0, $v1
		move $a0, $t0
		jal _print
L26_BS_Start:		nop
		li $v1, 999
		move $t0, $v1
		move $v0, $t0
		lw $s0, -12($fp)
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 12
		j $ra

		.text
		.globl BS_Search
BS_Search:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 40
		sw $s0, -12($fp)
		sw $s1, -16($fp)
		sw $s2, -20($fp)
		sw $s3, -24($fp)
		sw $s4, -28($fp)
		sw $s5, -32($fp)
		sw $s6, -36($fp)
		sw $s7, -40($fp)
		move $s0, $a0
		move $s1, $a1
		li $v1, 0
		move $t0, $v1
		move $s2, $t0
		li $v1, 0
		move $t0, $v1
		move $s3, $t0
		li $v1, 0
		move $t0, $v1
		move $s4, $t0
		li $v1, 0
		move $t0, $v1
		move $s5, $t0
		li $v1, 0
		move $t0, $v1
		move $s6, $t0
		li $v1, 0
		move $t0, $v1
		move $s7, $t0
		li $v1, 0
		move $t0, $v1
		li $v1, 0
		move $t0, $v1
		move $s7, $t0
		li $v1, 0
		move $t0, $v1
		move $s2, $t0
		move $t0, $s0
		lw $t0, 8($t0)
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L27_BS_Search
L27_BS_Search:		nop
		lw $t0, 0($t0)
		move $s3, $t0
		move $t0, $s3
		li $v1, 1
		move $t1, $v1
		sub $v1, $t0, $t1
		move $t0, $v1
		move $s3, $t0
		li $v1, 0
		move $t0, $v1
		move $s4, $t0
		li $v1, 1
		move $t0, $v1
		move $s5, $t0
L28_BS_Search:		move $t0, $s5
		beqz $t0, L29_BS_Search
		move $t0, $s4
		move $t1, $s3
		add $v1, $t0, $t1
		move $t0, $v1
		move $s6, $t0
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L30_BS_Search
L30_BS_Search:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 16($t1)
		move $t2, $s6
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		move $s6, $t0
		move $t0, $s0
		lw $t0, 8($t0)
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L31_BS_Search
L31_BS_Search:		nop
		move $t1, $s6
		move $t2, $t0
		lw $t2, 0($t2)
		li $v1, 1
		move $t3, $v1
		move $t4, $t1
		slt $v1, $t4, $t2
		move $t2, $v1
		sub $v1, $t3, $t2
		move $t2, $v1
		beqz $t2, L32_BS_Search
L32_BS_Search:		li $v1, 4
		move $t2, $v1
		li $v1, 1
		move $t3, $v1
		add $v1, $t3, $t1
		move $t1, $v1
		mul $v1, $t2, $t1
		move $t1, $v1
		add $v1, $t0, $t1
		move $t0, $v1
		lw $t0, 0($t0)
		move $s7, $t0
		move $t0, $s1
		move $t1, $s7
		slt $v1, $t0, $t1
		move $t0, $v1
		beqz $t0, L33_BS_Search
		move $t0, $s6
		li $v1, 1
		move $t1, $v1
		sub $v1, $t0, $t1
		move $t0, $v1
		move $s3, $t0
		b L34_BS_Search
L33_BS_Search:		nop
		move $t0, $s6
		li $v1, 1
		move $t1, $v1
		add $v1, $t0, $t1
		move $t0, $v1
		move $s4, $t0
L34_BS_Search:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L35_BS_Search
L35_BS_Search:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 4($t1)
		move $t2, $s7
		move $t3, $s1
		move $a0, $t0
		move $a1, $t2
		move $a2, $t3
		jalr $t1
		move $t0, $v0
		beqz $t0, L36_BS_Search
		li $v1, 0
		move $t0, $v1
		move $s5, $t0
		b L37_BS_Search
L36_BS_Search:		nop
		li $v1, 1
		move $t0, $v1
		move $s5, $t0
L37_BS_Search:		nop
		move $t0, $s3
		move $t1, $s4
		slt $v1, $t0, $t1
		move $t0, $v1
		beqz $t0, L38_BS_Search
		li $v1, 0
		move $t0, $v1
		move $s5, $t0
		b L39_BS_Search
L38_BS_Search:		nop
		li $v1, 0
		move $t0, $v1
L39_BS_Search:		nop
		b L28_BS_Search
L29_BS_Search:		nop
		move $t0, $s0
		move $t1, $t0
		li $v1, 1
		move $t2, $v1
		slt $v1, $t1, $t2
		move $t1, $v1
		beqz $t1, L40_BS_Search
L40_BS_Search:		nop
		move $t1, $t0
		lw $t1, 0($t1)
		lw $t1, 4($t1)
		move $t2, $s7
		move $t3, $s1
		move $a0, $t0
		move $a1, $t2
		move $a2, $t3
		jalr $t1
		move $t0, $v0
		beqz $t0, L41_BS_Search
		li $v1, 1
		move $t0, $v1
		move $s2, $t0
		b L42_BS_Search
L41_BS_Search:		nop
		li $v1, 0
		move $t0, $v1
		move $s2, $t0
L42_BS_Search:		nop
		move $t0, $s2
		move $v0, $t0
		lw $s0, -12($fp)
		lw $s1, -16($fp)
		lw $s2, -20($fp)
		lw $s3, -24($fp)
		lw $s4, -28($fp)
		lw $s5, -32($fp)
		lw $s6, -36($fp)
		lw $s7, -40($fp)
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 40
		j $ra

		.text
		.globl BS_Div
BS_Div:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a1
		li $v1, 0
		move $t1, $v1
		li $v1, 0
		move $t2, $v1
		li $v1, 0
		move $t3, $v1
		li $v1, 0
		move $t4, $v1
		move $t1, $t4
		li $v1, 0
		move $t4, $v1
		move $t2, $t4
		li $v1, 1
		move $t4, $v1
		sub $v1, $t0, $t4
		move $t0, $v1
		move $t3, $t0
L43_BS_Div:		move $t0, $t2
		move $t4, $t3
		slt $v1, $t0, $t4
		move $t0, $v1
		beqz $t0, L44_BS_Div
		move $t0, $t1
		li $v1, 1
		move $t4, $v1
		add $v1, $t0, $t4
		move $t0, $v1
		move $t1, $t0
		move $t0, $t2
		li $v1, 2
		move $t4, $v1
		add $v1, $t0, $t4
		move $t0, $v1
		move $t2, $t0
		b L43_BS_Div
L44_BS_Div:		nop
		move $t0, $t1
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl BS_Compare
BS_Compare:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t1, $a1
		move $t0, $a2
		li $v1, 0
		move $t2, $v1
		li $v1, 0
		move $t3, $v1
		li $v1, 0
		move $t4, $v1
		move $t2, $t4
		move $t4, $t0
		li $v1, 1
		move $t5, $v1
		add $v1, $t4, $t5
		move $t4, $v1
		move $t3, $t4
		move $t4, $t1
		slt $v1, $t4, $t0
		move $t0, $v1
		beqz $t0, L45_BS_Compare
		li $v1, 0
		move $t0, $v1
		move $t2, $t0
		b L46_BS_Compare
L45_BS_Compare:		nop
		li $v1, 1
		move $t0, $v1
		slt $v1, $t1, $t3
		move $t1, $v1
		sub $v1, $t0, $t1
		move $t0, $v1
		beqz $t0, L47_BS_Compare
		li $v1, 0
		move $t0, $v1
		move $t2, $t0
		b L48_BS_Compare
L47_BS_Compare:		nop
		li $v1, 1
		move $t0, $v1
		move $t2, $t0
L48_BS_Compare:		nop
L46_BS_Compare:		nop
		move $t0, $t2
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl BS_Print
BS_Print:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a0
		li $v1, 0
		move $t1, $v1
		li $v1, 1
		move $t2, $v1
		move $t1, $t2
L49_BS_Print:		move $t2, $t1
		move $t3, $t0
		lw $t3, 4($t3)
		slt $v1, $t2, $t3
		move $t2, $v1
		beqz $t2, L50_BS_Print
		move $t2, $t0
		lw $t2, 8($t2)
		move $t3, $t2
		li $v1, 1
		move $t4, $v1
		slt $v1, $t3, $t4
		move $t3, $v1
		beqz $t3, L51_BS_Print
L51_BS_Print:		nop
		move $t3, $t1
		move $t4, $t2
		lw $t4, 0($t4)
		li $v1, 1
		move $t5, $v1
		move $t6, $t3
		slt $v1, $t6, $t4
		move $t4, $v1
		sub $v1, $t5, $t4
		move $t4, $v1
		beqz $t4, L52_BS_Print
L52_BS_Print:		li $v1, 4
		move $t4, $v1
		li $v1, 1
		move $t5, $v1
		add $v1, $t5, $t3
		move $t3, $v1
		mul $v1, $t4, $t3
		move $t3, $v1
		add $v1, $t2, $t3
		move $t2, $v1
		lw $t2, 0($t2)
		move $a0, $t2
		jal _print
		move $t2, $t1
		li $v1, 1
		move $t3, $v1
		add $v1, $t2, $t3
		move $t2, $v1
		move $t1, $t2
		b L49_BS_Print
L50_BS_Print:		nop
		li $v1, 99999
		move $t0, $v1
		move $a0, $t0
		jal _print
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl BS_Init
BS_Init:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 12
		sw $s0, -12($fp)
		move $t1, $a0
		move $t0, $a1
		li $v1, 0
		move $t2, $v1
		li $v1, 0
		move $t3, $v1
		move $s0, $t3
		li $v1, 0
		move $t4, $v1
		li $v1, 0
		move $t5, $v1
		move $t6, $t1
		move $t7, $t0
		sw $t7, 4($t6)
		move $t6, $t1
		li $v1, 4
		move $t7, $v1
		li $v1, 1
		move $t8, $v1
		move $t9, $t0
		add $v1, $t8, $t9
		move $t8, $v1
		mul $v1, $t7, $t8
		move $t7, $v1
		move $a0, $t7
		jal _halloc
		move $t7, $v0
		move $t8, $t7
		move $t9, $t0
		sw $t9, 0($t8)
L53_BS_Init:		li $v1, 0
		move $t8, $v1
		move $t9, $t0
		slt $v1, $t8, $t9
		move $t8, $v1
		beqz $t8, L54_BS_Init
		move $t8, $t7
		li $v1, 4
		move $t9, $v1
		move $t3, $t0
		mul $v1, $t9, $t3
		move $t3, $v1
		add $v1, $t8, $t3
		move $t3, $v1
		li $v1, 0
		move $t8, $v1
		sw $t8, 0($t3)
		move $t3, $t0
		li $v1, 1
		move $t8, $v1
		sub $v1, $t3, $t8
		move $t3, $v1
		move $t0, $t3
		b L53_BS_Init
L54_BS_Init:		nop
		move $t0, $t7
		sw $t0, 8($t6)
		li $v1, 1
		move $t0, $v1
		move $t2, $t0
		move $t0, $t1
		lw $t0, 4($t0)
		li $v1, 1
		move $t3, $v1
		add $v1, $t0, $t3
		move $t0, $v1
		move $s0, $t0
L55_BS_Init:		move $t0, $t2
		move $t3, $t1
		lw $t3, 4($t3)
		slt $v1, $t0, $t3
		move $t0, $v1
		beqz $t0, L56_BS_Init
		li $v1, 2
		move $t0, $v1
		move $t3, $t2
		mul $v1, $t0, $t3
		move $t0, $v1
		move $t5, $t0
		move $t0, $s0
		li $v1, 3
		move $t3, $v1
		sub $v1, $t0, $t3
		move $t0, $v1
		move $t4, $t0
		move $t0, $t1
		lw $t0, 8($t0)
		move $t3, $t0
		li $v1, 1
		move $t6, $v1
		slt $v1, $t3, $t6
		move $t3, $v1
		beqz $t3, L57_BS_Init
L57_BS_Init:		nop
		move $t3, $t2
		move $t6, $t0
		lw $t6, 0($t6)
		li $v1, 1
		move $t7, $v1
		move $t8, $t3
		slt $v1, $t8, $t6
		move $t6, $v1
		sub $v1, $t7, $t6
		move $t6, $v1
		beqz $t6, L58_BS_Init
L58_BS_Init:		li $v1, 4
		move $t6, $v1
		li $v1, 1
		move $t7, $v1
		add $v1, $t7, $t3
		move $t3, $v1
		mul $v1, $t6, $t3
		move $t3, $v1
		add $v1, $t0, $t3
		move $t0, $v1
		move $t3, $t5
		add $v1, $t3, $t4
		move $t3, $v1
		sw $t3, 0($t0)
		move $t0, $t2
		li $v1, 1
		move $t3, $v1
		add $v1, $t0, $t3
		move $t0, $v1
		move $t2, $t0
		move $t0, $s0
		li $v1, 1
		move $t3, $v1
		sub $v1, $t0, $t3
		move $t0, $v1
		move $s0, $t0
		b L55_BS_Init
L56_BS_Init:		nop
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $s0, -12($fp)
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 12
		j $ra

		
		.text
		.globl _halloc
		_halloc:
		li $v0, 9
		syscall
		j $ra
		.text
		.globl _print
		_print:
		li $v0, 1
		syscall
		la $a0, newl
		li $v0, 4
		syscall
		j $ra
		.data
		.align   0
		newl:
		.asciiz "\n"
		.data
		.align   0
		str_er:
		.asciiz " ERROR: abnormal termination\n"
