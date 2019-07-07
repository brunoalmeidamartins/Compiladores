		.text
		.globl main
main:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		li $v1, 16
		move $a0, $v1
		jal _halloc
		move $t0, $v0
		li $v1, 12
		move $a0, $v1
		jal _halloc
		move $t1, $v0
		la $v1, LS_Init
		move $t2, $v1
		sw $t2, 12($t0)
		la $v1, LS_Search
		move $t2, $v1
		sw $t2, 8($t0)
		la $v1, LS_Print
		move $t2, $v1
		sw $t2, 4($t0)
		la $v1, LS_Start
		move $t2, $v1
		sw $t2, 0($t0)
		li $v1, 4
		move $t2, $v1
L0_MAIN:		nop
		li $v1, 12
		move $t3, $v1
		slt $v1, $t2, $t3
		move $t3, $v1
		beqz $t3, L1_MAIN
		add $v1, $t1, $t2
		move $t3, $v1
		li $v1, 0
		move $t4, $v1
		sw $t4, 0($t3)
		li $v1, 4
		add $v1, $t2, $v1
		move $t2, $v1
		b L0_MAIN
L1_MAIN:		nop
		sw $t0, 0($t1)
		move $t0, $t1
		lw $t1, 0($t0)
		lw $t1, 0($t1)
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
		.globl LS_Start
LS_Start:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 12
		sw $s0, -12($fp)
		move $s0, $a0
		move $t0, $a1
		move $t1, $s0
		lw $t2, 0($t1)
		lw $t2, 12($t2)
		move $a0, $t1
		move $a1, $t0
		jalr $t2
		move $t0, $v0
		move $t0, $s0
		lw $t1, 0($t0)
		lw $t1, 4($t1)
		move $a0, $t0
		jalr $t1
		move $t0, $v0
		li $v1, 9999
		move $t0, $v1
		move $a0, $t0
		jal _print
		move $t0, $s0
		lw $t1, 0($t0)
		lw $t1, 8($t1)
		li $v1, 8
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		move $a0, $t0
		jal _print
		move $t0, $s0
		lw $t1, 0($t0)
		lw $t1, 8($t1)
		li $v1, 12
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		move $a0, $t0
		jal _print
		move $t0, $s0
		lw $t1, 0($t0)
		lw $t1, 8($t1)
		li $v1, 17
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		move $a0, $t0
		jal _print
		move $t0, $s0
		lw $t1, 0($t0)
		lw $t1, 8($t1)
		li $v1, 50
		move $t2, $v1
		move $a0, $t0
		move $a1, $t2
		jalr $t1
		move $t0, $v0
		move $a0, $t0
		jal _print
		li $v1, 55
		move $t0, $v1
		move $v0, $t0
		lw $s0, -12($fp)
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 12
		j $ra

		.text
		.globl LS_Print
LS_Print:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a0
		li $v1, 1
		move $t1, $v1
L2_LS_Print:		nop
		lw $t2, 8($t0)
		slt $v1, $t1, $t2
		move $t2, $v1
		beqz $t2, L3_LS_Print
		lw $t2, 4($t0)
		li $v1, 4
		mul $v1, $t1, $v1
		move $t3, $v1
		lw $t2, 4($t0)
		lw $t4, 0($t2)
		li $v1, 1
		move $t5, $v1
		slt $v1, $t3, $t4
		move $t4, $v1
		sub $v1, $t5, $t4
		move $t4, $v1
		beqz $t4, L4_LS_Print
L4_LS_Print:		nop
		li $v1, 4
		move $t4, $v1
		add $v1, $t3, $t4
		move $t3, $v1
		add $v1, $t2, $t3
		move $t2, $v1
		lw $t2, 0($t2)
		move $a0, $t2
		jal _print
		li $v1, 1
		add $v1, $t1, $v1
		move $t1, $v1
		b L2_LS_Print
L3_LS_Print:		nop
		li $v1, 0
		move $t0, $v1
		move $v0, $t0
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl LS_Search
LS_Search:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t0, $a0
		move $t1, $a1
		li $v1, 1
		move $t2, $v1
		li $v1, 0
		move $t3, $v1
		li $v1, 0
		move $t3, $v1
L5_LS_Search:		nop
		lw $t4, 8($t0)
		slt $v1, $t2, $t4
		move $t4, $v1
		beqz $t4, L6_LS_Search
		lw $t4, 4($t0)
		li $v1, 4
		mul $v1, $t2, $v1
		move $t5, $v1
		lw $t4, 4($t0)
		lw $t6, 0($t4)
		li $v1, 1
		move $t7, $v1
		slt $v1, $t5, $t6
		move $t6, $v1
		sub $v1, $t7, $t6
		move $t6, $v1
		beqz $t6, L7_LS_Search
L7_LS_Search:		nop
		li $v1, 4
		move $t6, $v1
		add $v1, $t5, $t6
		move $t5, $v1
		add $v1, $t4, $t5
		move $t4, $v1
		lw $t4, 0($t4)
		li $v1, 1
		add $v1, $t1, $v1
		move $t5, $v1
		slt $v1, $t4, $t1
		move $t6, $v1
		beqz $t6, L8_LS_Search
		li $v1, 0
		move $t6, $v1
		b L9_LS_Search
L8_LS_Search:		nop
		li $v1, 1
		move $t6, $v1
		slt $v1, $t4, $t5
		move $t4, $v1
		sub $v1, $t6, $t4
		move $t4, $v1
		beqz $t4, L10_LS_Search
		li $v1, 0
		move $t6, $v1
		b L11_LS_Search
L10_LS_Search:		nop
		li $v1, 1
		move $t3, $v1
		li $v1, 1
		move $t3, $v1
		lw $t4, 8($t0)
		move $t2, $t4
L11_LS_Search:		nop
L9_LS_Search:		nop
		li $v1, 1
		add $v1, $t2, $v1
		move $t2, $v1
		b L5_LS_Search
L6_LS_Search:		nop
		move $v0, $t3
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl LS_Init
LS_Init:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		move $t1, $a0
		move $t0, $a1
		sw $t0, 8($t1)
		li $v1, 1
		add $v1, $t0, $v1
		move $t2, $v1
		li $v1, 4
		move $t3, $v1
		mul $v1, $t2, $t3
		move $t2, $v1
		move $a0, $t2
		jal _halloc
		move $t2, $v0
		li $v1, 4
		move $t3, $v1
L12_LS_Init:		nop
		li $v1, 1
		move $t4, $v1
		add $v1, $t0, $t4
		move $t4, $v1
		li $v1, 4
		move $t5, $v1
		mul $v1, $t4, $t5
		move $t4, $v1
		slt $v1, $t3, $t4
		move $t4, $v1
		beqz $t4, L13_LS_Init
		add $v1, $t2, $t3
		move $t4, $v1
		li $v1, 0
		move $t5, $v1
		sw $t5, 0($t4)
		li $v1, 4
		add $v1, $t3, $v1
		move $t3, $v1
		b L12_LS_Init
L13_LS_Init:		nop
		li $v1, 4
		move $t3, $v1
		mul $v1, $t0, $t3
		move $t0, $v1
		sw $t0, 0($t2)
		sw $t2, 4($t1)
		li $v1, 1
		move $t0, $v1
		lw $t2, 8($t1)
		li $v1, 1
		move $t3, $v1
		add $v1, $t2, $t3
		move $t2, $v1
L14_LS_Init:		nop
		lw $t3, 8($t1)
		slt $v1, $t0, $t3
		move $t3, $v1
		beqz $t3, L15_LS_Init
		li $v1, 2
		move $t3, $v1
		mul $v1, $t3, $t0
		move $t3, $v1
		li $v1, 3
		sub $v1, $t2, $v1
		move $t4, $v1
		li $v1, 1
		move $t5, $v1
		li $v1, 4
		mul $v1, $t5, $v1
		move $t5, $v1
		add $v1, $t1, $t5
		move $t6, $v1
		lw $t6, 0($t6)
		li $v1, 4
		mul $v1, $t0, $v1
		move $t7, $v1
		li $v1, 1
		move $t8, $v1
		li $v1, 4
		mul $v1, $t8, $v1
		move $t5, $v1
		add $v1, $t1, $t5
		move $t5, $v1
		lw $t6, 0($t5)
		lw $t5, 0($t6)
		li $v1, 1
		move $t8, $v1
		slt $v1, $t7, $t5
		move $t5, $v1
		sub $v1, $t8, $t5
		move $t5, $v1
		beqz $t5, L16_LS_Init
L16_LS_Init:		nop
		li $v1, 4
		move $t5, $v1
		add $v1, $t7, $t5
		move $t5, $v1
		add $v1, $t6, $t5
		move $t5, $v1
		add $v1, $t3, $t4
		move $t3, $v1
		sw $t3, 0($t5)
		li $v1, 1
		add $v1, $t0, $v1
		move $t0, $v1
		li $v1, 1
		sub $v1, $t2, $v1
		move $t2, $v1
		b L14_LS_Init
L15_LS_Init:		nop
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
