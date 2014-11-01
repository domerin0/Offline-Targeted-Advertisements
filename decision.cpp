/* Decision recieves a a ratio of men/women and number of people
	Returns Type of ad to display*/

unsigned int ratio;
unsigned int people;
unsigned int  gender = 3;
unsigned int multi = 0;

int decision(ratio, people){
	
	//If the ratio is not %100 male or female, play default ad 
	gender = ratioCheck(ratio);
	
	if (people >1){
	 multi = 1;
	}
	//if Man
	if (gender == 1){
		if (multi == 1){
			return 1; //Multiple Men
		}
		else{
			return 2;// Singular Man
		}
	}
	//if Woman
	elseif (gender == 0) {
		if (multi == 1){
			return 3; //Multiple Women
		}
		else{
			return 4; //Singular Woman
		}
	}	
}

int ratioCheck(ratio){
	if (ratio == 0){
		return 0;//all women
	}
	
	elseif (ratio == 1){
		return 1; //all men
	}

	else {
		return 2;
	}
}
