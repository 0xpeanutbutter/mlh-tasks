.globl main
.text

main:

 
la $v0,4
la $a0,str
syscall

la $v0,5
syscall
move $t0,$v0

li $t1,0
li $t2,1
la $v0,1
la $a0,0($t1)
syscall
la $v0,4
la $a0,n
syscall
la $v0,1
la $a0,0($t2)
syscall
la $v0,4
la $a0,n
syscall
la $t4,n
L1:

bne $t0,2,L2
j exit

L2:
add $t3,$t2,$t1
la $v0,1
la $a0,0($t3)
syscall
la $v0,4
la $a0,n
syscall

move $t1,$t2
move $t2,$t3
addi $t0,$t0,-1
j L1

exit:
la $v0,10
syscall
.end main


 
.data
str: .asciiz "Enter the length of series : "
n: .asciiz " "