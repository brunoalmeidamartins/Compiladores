		.text
		.globl main
main:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		li $v1, 12
		move $a0, $v1
		jal _halloc
		move $t0, $v0
		la $v1, BBS_vTable
		move $t1, $v1
		lw $t1, 0($t1)
		sw $t1, 0($t0)
		li $v1, 0
		move $t1, $v1
		sw $t1, 4($t0)
		sw $t1, 8($t0)
		li $v1, 16
		move $a0, $v1
		jal _halloc
		move $t1, $v0
		sw $t1, 0($t0)
		la $v1, BBS_Start
		move $t2, $v1
		sw $t2, 0($t1)
		la $v1, BBS_Sort
		move $t2, $v1
		sw $t2, 4($t1)
		la $v1, BBS_Print
		move $t2, $v1
		sw $t2, 8($t1)
		la $v1, BBS_Init
		move $t2, $v1
		sw $t2, 12($t1)
		lw $t1, 0($t0)
		lw $t1, 16($t1)
		li $v1, 10
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
		.globl BBS_Start
BBS_Start:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 12
		sw $s0, -12($fp)
		move $s0, $a0
		lw $t0, 0($s0)
		lw $t0, 16($t0)
		move $a0, $s0
		move $a1, $t0
		jalr $t0
		move $t0, $v0
		lw $t0, 0($s0)
		lw $t0, 16($t0)
		move $a0, $s0
		jalr $t0
		move $t0, $v0
		li $v1, 99999
		move $t0, $v1
		move $a0, $t0
		jal _print
		lw $t0, 0($s0)
		lw $t0, 16($t0)
		move $a0, $s0
		jalr $t0
		move $t0, $v0
		lw $t0, 0($s0)
		lw $t0, 16($t0)
		move $a0, $s0
		jalr $t0
		move $t0, $v0
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $s0, -12($fp)
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 12
		j $ra

		.text
		.globl BBS_Sort
BBS_Sort:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a0
		li $v1, 8
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		li $v1, 1
		move $t2, $v1
		sub $v1, $t1, $t2
		move $t1, $v1
		li $v1, 0
		move $t2, $v1
		li $v1, 1
		move $t3, $v1
		sub $v1, $t2, $t3
		move $t2, $v1
L1_BBS_Sort:		nop
		slt $v1, $t2, $t1
		move $t3, $v1
		beqz $t3, L2_BBS_Sort
		li $v1, 1
		move $t3, $v1
L3_BBS_Sort:		nop
		li $v1, 1
		move $t4, $v1
		add $v1, $t1, $t4
		move $t4, $v1
		slt $v1, $t3, $t4
		move $t4, $v1
		beqz $t4, L4_BBS_Sort
		li $v1, 1
		move $t4, $v1
		sub $v1, $t3, $t4
		move $t4, $v1
		li $v1, 4
		add $v1, $t0, $v1
		move $t5, $v1
		lw $t5, 0($t5)
		lw $t6, 0($t5)
		li $v1, 0
		slt $v1, $t4, $v1
		move $t7, $v1
		beqz $t7, L6_BBS_Sort
L6_BBS_Sort:		nop
		slt $v1, $t4, $t6
		move $t7, $v1
		li $v1, 1
		move $t6, $v1
		sub $v1, $t6, $t7
		move $t7, $v1
		beqz $t7, L5_BBS_Sort
L5_BBS_Sort:		nop
		li $v1, 4
		mul $v1, $t4, $v1
		move $t4, $v1
		add $v1, $t5, $t4
		move $t4, $v1
		lw $t4, 4($t4)
		li $v1, 4
		add $v1, $t0, $v1
		move $t5, $v1
		lw $t5, 0($t5)
		lw $t6, 0($t5)
		li $v1, 0
		slt $v1, $t3, $v1
		move $t7, $v1
		beqz $t7, L8_BBS_Sort
L8_BBS_Sort:		nop
		slt $v1, $t3, $t6
		move $t7, $v1
		li $v1, 1
		move $t6, $v1
		sub $v1, $t6, $t7
		move $t7, $v1
		beqz $t7, L7_BBS_Sort
L7_BBS_Sort:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t6, $v1
		add $v1, $t5, $t6
		move $t6, $v1
		lw $t5, 4($t6)
		slt $v1, $t5, $t4
		move $t4, $v1
		beqz $t4, L9_BBS_Sort
		li $v1, 1
		move $t4, $v1
		sub $v1, $t3, $t4
		move $t4, $v1
		li $v1, 4
		add $v1, $t0, $v1
		move $t5, $v1
		lw $t5, 0($t5)
		lw $t6, 0($t5)
		li $v1, 0
		slt $v1, $t4, $v1
		move $t7, $v1
		beqz $t7, L12_BBS_Sort
L12_BBS_Sort:		nop
		slt $v1, $t4, $t6
		move $t7, $v1
		li $v1, 1
		move $t6, $v1
		sub $v1, $t6, $t7
		move $t7, $v1
		beqz $t7, L11_BBS_Sort
L11_BBS_Sort:		nop
		li $v1, 4
		mul $v1, $t4, $v1
		move $t6, $v1
		add $v1, $t5, $t6
		move $t6, $v1
		lw $t5, 4($t6)
		li $v1, 4
		add $v1, $t0, $v1
		move $t6, $v1
		lw $t6, 0($t6)
		lw $t7, 0($t6)
		li $v1, 0
		slt $v1, $t4, $v1
		move $t8, $v1
		beqz $t8, L13_BBS_Sort
		slt $v1, $t4, $t7
		move $t8, $v1
		li $v1, 1
		move $t7, $v1
		sub $v1, $t7, $t8
		move $t8, $v1
L13_BBS_Sort:		beqz $t8, L14_BBS_Sort
L14_BBS_Sort:		nop
		li $v1, 4
		mul $v1, $t4, $v1
		move $t4, $v1
		add $v1, $t6, $t4
		move $t4, $v1
		li $v1, 4
		add $v1, $t0, $v1
		move $t6, $v1
		lw $t6, 0($t6)
		lw $t7, 0($t6)
		li $v1, 0
		slt $v1, $t3, $v1
		move $t8, $v1
		beqz $t8, L16_BBS_Sort
L16_BBS_Sort:		nop
		slt $v1, $t3, $t7
		move $t8, $v1
		li $v1, 1
		move $t7, $v1
		sub $v1, $t7, $t8
		move $t8, $v1
		beqz $t8, L15_BBS_Sort
L15_BBS_Sort:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t7, $v1
		add $v1, $t6, $t7
		move $t7, $v1
		lw $t6, 4($t7)
		sw $t6, 4($t4)
		li $v1, 4
		add $v1, $t0, $v1
		move $t4, $v1
		lw $t4, 0($t4)
		lw $t6, 0($t4)
		li $v1, 0
		slt $v1, $t3, $v1
		move $t7, $v1
		beqz $t7, L17_BBS_Sort
		slt $v1, $t3, $t6
		move $t7, $v1
		li $v1, 1
		move $t6, $v1
		sub $v1, $t6, $t7
		move $t7, $v1
L17_BBS_Sort:		beqz $t7, L18_BBS_Sort
L18_BBS_Sort:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t6, $v1
		add $v1, $t4, $t6
		move $t4, $v1
		sw $t5, 4($t4)
		b L10_BBS_Sort
L9_BBS_Sort:		nop
		li $v1, 0
		move $t4, $v1
L10_BBS_Sort:		nop
		li $v1, 1
		move $t4, $v1
		add $v1, $t3, $t4
		move $t4, $v1
		move $t3, $t4
		b L3_BBS_Sort
L4_BBS_Sort:		nop
		li $v1, 1
		move $t3, $v1
		sub $v1, $t1, $t3
		move $t3, $v1
		move $t1, $t3
		b L1_BBS_Sort
L2_BBS_Sort:		nop
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl BBS_Print
BBS_Print:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a0
		li $v1, 0
		move $t1, $v1
L19_BBS_Print:		nop
		li $v1, 8
		add $v1, $t0, $v1
		move $t2, $v1
		lw $t2, 0($t2)
		slt $v1, $t1, $t2
		move $t2, $v1
		beqz $t2, L20_BBS_Print
		li $v1, 4
		add $v1, $t0, $v1
		move $t2, $v1
		lw $t2, 0($t2)
		lw $t3, 0($t2)
		li $v1, 0
		slt $v1, $t1, $v1
		move $t4, $v1
		beqz $t4, L22_BBS_Print
L22_BBS_Print:		nop
		slt $v1, $t1, $t3
		move $t4, $v1
		li $v1, 1
		move $t3, $v1
		sub $v1, $t3, $t4
		move $t4, $v1
		beqz $t4, L21_BBS_Print
L21_BBS_Print:		nop
		li $v1, 4
		mul $v1, $t1, $v1
		move $t3, $v1
		add $v1, $t2, $t3
		move $t3, $v1
		lw $t2, 4($t3)
		move $a0, $t2
		jal _print
		li $v1, 1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t2, $v1
		move $t1, $t2
		b L19_BBS_Print
L20_BBS_Print:		nop
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl BBS_Init
BBS_Init:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a0
		li $v1, 8
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t2, 0($t1)
		sw $t1, 0($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t2, $v1
		lw $t3, 0($t2)
		li $v1, 1
		slt $v1, $t1, $v1
		move $t3, $v1
		beqz $t3, L23_BBS_Init
L23_BBS_Init:		nop
		li $v1, 1
		add $v1, $t1, $v1
		move $t3, $v1
		li $v1, 4
		mul $v1, $t3, $v1
		move $t3, $v1
		move $a0, $t3
		jal _halloc
		move $t3, $v0
		sw $t1, 0($t3)
		li $v1, 1
		move $t4, $v1
		li $v1, 4
		add $v1, $t3, $v1
		move $t5, $v1
		li $v1, 1
		move $t6, $v1
		li $v1, 0
		move $t7, $v1
L24_BBS_Init:		beqz $t4, L25_BBS_Init
		sw $t7, 0($t5)
		li $v1, 4
		add $v1, $t5, $v1
		move $t5, $v1
		li $v1, 1
		sub $v1, $t1, $v1
		move $t1, $v1
		li $v1, 1
		slt $v1, $t1, $v1
		move $t4, $v1
		sub $v1, $t6, $t4
		move $t4, $v1
		b L24_BBS_Init
L25_BBS_Init:		nop
		sw $t3, 0($t2)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 0
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L26_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L26_BBS_Init:		beqz $t4, L27_BBS_Init
L27_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 20
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 1
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L28_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L28_BBS_Init:		beqz $t4, L29_BBS_Init
L29_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 7
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 2
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L30_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L30_BBS_Init:		beqz $t4, L31_BBS_Init
L31_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 12
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 3
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L32_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L32_BBS_Init:		beqz $t4, L33_BBS_Init
L33_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 18
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 4
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L34_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L34_BBS_Init:		beqz $t4, L35_BBS_Init
L35_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 2
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 5
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L36_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L36_BBS_Init:		beqz $t4, L37_BBS_Init
L37_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 11
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 6
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L38_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L38_BBS_Init:		beqz $t4, L39_BBS_Init
L39_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 6
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 7
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L40_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L40_BBS_Init:		beqz $t4, L41_BBS_Init
L41_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 9
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t1, $v1
		lw $t1, 0($t1)
		lw $t2, 0($t1)
		li $v1, 8
		move $t3, $v1
		li $v1, 0
		slt $v1, $t3, $v1
		move $t4, $v1
		beqz $t4, L42_BBS_Init
		slt $v1, $t3, $t2
		move $t4, $v1
		li $v1, 1
		move $t2, $v1
		sub $v1, $t2, $t4
		move $t4, $v1
L42_BBS_Init:		beqz $t4, L43_BBS_Init
L43_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t3, $v1
		move $t2, $v1
		add $v1, $t1, $t2
		move $t1, $v1
		li $v1, 19
		move $t2, $v1
		sw $t2, 4($t1)
		li $v1, 4
		add $v1, $t0, $v1
		move $t0, $v1
		lw $t0, 0($t0)
		lw $t1, 0($t0)
		li $v1, 9
		move $t2, $v1
		li $v1, 0
		slt $v1, $t2, $v1
		move $t3, $v1
		beqz $t3, L44_BBS_Init
		slt $v1, $t2, $t1
		move $t3, $v1
		li $v1, 1
		move $t1, $v1
		sub $v1, $t1, $t3
		move $t3, $v1
L44_BBS_Init:		beqz $t3, L45_BBS_Init
L45_BBS_Init:		nop
		li $v1, 4
		mul $v1, $t2, $v1
		move $t1, $v1
		add $v1, $t0, $t1
		move $t0, $v1
		li $v1, 5
		move $t1, $v1
		sw $t1, 4($t0)
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
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
