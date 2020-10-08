function sumn

{
	
	if [ $1 -eq 1 ];then

	return 1
	
	fi

	sumn $(($1-1))

	ret=$?

	sumt=$(($ret+$1))

	return $sumt

}

echo "enter a no.:"

read n

sumn $n

retu=$?

echo "sum is : $retu"
