/*

var pyramidText = 
	'            /*\\         ___\n' +
	' \\|/       /***\\       (___)\n' +
	' -o-      /*****\\          ___\n' +
	' /|\\     /***o***\\        (___)\n' +
	'        /*********\\\n' +
	'       /***********\\              ___\n' +
	'      /******o******\\            (   )\n' +
	'     /***************\\      v    (   )\n' +
	'    /*****************\\   v      (   )\n' +
	'   /*********o*********\\         (   )\n' +
	'  /*********************\\        (___)\n' +
	' /***********************\\        | |\n' +
	'/********|      -|********\\       | |\n';

*/
var pyramidText = '';

document.getElementById('pyramid').children[0].innerHTML =
	'            /*\\         ___\n' +
	' \\|/       /***\\       (___)\n' +
	' -o-      /*****\\          ___\n' +
	' /|\\     /***o***\\        (___)\n' +
	'        /*********\\\n' +
	'       /***********\\              ___\n' +
	'      /******o******\\            (   )\n' +
	'     /***************\\      v    (   )\n' +
	'    /*****************\\   v      (   )\n' +
	'   /*********o*********\\         (   )\n' +
	'  /*********************\\        (___)\n' +
	' /***********************\\        | |\n' +
	'/********|      -|********\\       | |\n';
// Ne rien modifier au dessus de ce commentaire

// Fonction qui permet de choisir une hauteur personnalisé
// Ne pas modifier cette fonction
function ownSize() {
	var size = Number(prompt("Choisissez une hauteur :"));
	if (size != null && size > 0) {
		pyramid(size);
	}
}

// Fonction qui permet de recommencer
function restart() {
	pyramidText = '';
	// Ne rien modifier au dessus de ce commentaire

	// Ne rien modifier au dessous de ce commentaire
	document.getElementById('pyramid').children[0].innerHTML =
		'            /*\\         ___\n' +
		' \\|/       /***\\       (___)\n' +
		' -o-      /*****\\          ___\n' +
		' /|\\     /***o***\\        (___)\n' +
		'        /*********\\\n' +
		'       /***********\\              ___\n' +
		'      /******o******\\            (   )\n' +
		'     /***************\\      v    (   )\n' +
		'    /*****************\\   v      (   )\n' +
		'   /*********o*********\\         (   )\n' +
		'  /*********************\\        (___)\n' +
		' /***********************\\        | |\n' +
		'/********|      -|********\\       | |\n';
}

// Fonction pour dessiner la pyramid
function pyramid(size) {
	pyramidText = '';
	// Ne rien modifier au dessus de ce commentaire

	// Ne rien modifier au dessous de ce commentaire
	document.getElementById('pyramid').children[0].innerHTML = pyramidText;
}

