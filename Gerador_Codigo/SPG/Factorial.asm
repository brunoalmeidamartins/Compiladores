		.text
		.globl main
main:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 8
		li $v1, 4
		move $a0, $v1
		jal _halloc
		move $t0, $v0
		li $v1, 4
		move $a0, $v1
		jal _halloc
		move $t1, $v0
		la $v1, Fac_ComputeFac
		move $t2, $v1
		sw $t2, 0($t0)
		sw $t0, 0($t1)
		move $t0, $t1
		lw $t1, 0($t0)
		lw $t2, 0($t1)
		li $v1, 10
		move $t1, $v1
		move $a0, $t0
		move $a1, $t1
		jalr $t2
		move $t3, $v0
		move $a0, $t3
		jal _print
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 8
		j $ra

		.text
		.globl Fac_ComputeFac
Fac_ComputeFac:
		sw $fp, -8($sp)
		sw $ra, -4($sp)
		move $fp, $sp
		subu $sp, $sp, 20
		sw $s0, -12($fp)
		sw $s1, -16($fp)
		sw $s2, -20($fp)
		move $s0, $a0
		move $s1, $a1
		li $v1, 1
		move $t0, $v1
		slt $v1, $s1, $t0
		move $t1, $v1
		beqz $t1, L2
		li $v1, 1
		move $s2, $v1
		b L3
L2:		nop
		move $t0, $s0
		lw $t1, 0($t0)
		lw $t2, 0($t1)
		li $v1, 1
		move $t1, $v1
		sub $v1, $s1, $t1
		move $t3, $v1
		move $a0, $t0
		move $a1, $t3
		jalr $t2
		move $t1, $v0
		mul $v1, $s1, $t1
		move $t0, $v1
		move $s2, $t0
L3:		nop
		move $v0, $s2
		lw $s0, -12($fp)
		lw $s1, -16($fp)
		lw $s2, -20($fp)
		lw $ra, -4($fp)
		lw $fp, -8($fp)
		addu $sp, $sp, 20
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
