var CodageGroupSize = 0;
var CodageTableChar = "";


	CodageTableChar = "0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&~#|*+-\\/=%!:;?,.<>'àâçéèêëïîöôüûù" + '"';
	TableConv.value = CodageTableChar;
	
function standard(entree)
{
  alphabet= '0123456789';
  longueur = entree.length;

  entree_standard='';
  for (i=0; i<longueur; i++)
  {
    if (alphabet.indexOf(entree.charAt(i))!=-1)
    {
      entree_standard += entree.charAt(i)
    }
  }
  return entree_standard;
}


// calcul les différentes clefs nécessaires

  p = (P.value == "") ? 0 : P.value;
  q = (Q.value == "") ? 0 : Q.value;
  n = p * q;
  N.value = parseFloat( n);
  Euler = n - p - q + 1;

  // Recherche au coup par coup
  e = (E.value == "") ? 0 : E.value;
  TmpNe = 1;
  d = 1;
  while
   (((d * e) % Euler) != 1)
    {
    TmpNe += 1;
    d = Math.ceil( TmpNe * Euler / e);
    };
  D.value = parseFloat(d);

  // vérification si codage sera valable
  CodageGroupSize = Groupage.value;
  if (CodageTableChar.length*Math.pow(100, CodageGroupSize - 1) > n)
    {
    alert("P ou Q risquent d'être trop petits pour un chiffrement valable !");
    };
  


function ValeurChar(Lettre)
  {
  return (CodageTableChar.indexOf(Lettre, 0));
  };


// Calcul le modulo "Modulo" de "Base" a la puissance "Exposant"
function ModuloDexpo(Base, Exposant, Modulo)
  {
  var ModuloBase2 = new Array();

  // Niveau de puissance de 2 à considérer
  ModuloLevel = Math.max(Math.floor((Math.log(Exposant) / 0.6931471805599)), 1);

  // Préparation du tableau de transcodage
  ModuloBase2[ 0] = Base % Modulo;
  for
   ( Level = 1; Level <= ModuloLevel; Level++)
     {
     ModuloBase2[ Level] = ( ModuloBase2[ Level - 1] * ModuloBase2[ Level - 1]) % Modulo;
     };

  // Utilisation pour décomposition en utilisant le tableau
  ExpoDec = Exposant;
  Valeur = 1;
  Level = ModuloLevel;
  while
   (ExpoDec > 0)
     {
     if
      (ExpoDec >= Math.pow(2, Level))
       {
       Valeur = (Valeur * ModuloBase2[ Level]) % Modulo;
       ExpoDec -= Math.pow(2, Level--);
       }
      else
       {
       Level--
       };
     }
  return Valeur
  };


function Encodage(Message, E, N)
  {
  messageNum="";
  PreSize = Math.ceil(Math.log(N) / Math.LN10);
  TailleGroupe = parseInt(Groupage.value)
  CodageTableChar = TableConv.value;
  for(k=0; k<Message.length; k++) {
	chiffre=ValeurChar(Message.charAt(k))
	if(parseInt(chiffre)<10) {chiffre="0"+chiffre};
	messageNum+=chiffre
    }
	while(messageNum.length%TailleGroupe>0){messageNum="0"+messageNum}
    MessageCode="";
    for(k=0; k<messageNum.length; k=k+TailleGroupe) {
		GroupeValue=parseInt(messageNum.substring(k,k+TailleGroupe),10)
    	// chiffre le groupe
    	GroupePreCode = ModuloDexpo(GroupeValue, E, N);
	xx=GroupePreCode.toString()
	while(xx.length<PreSize) {GroupePreCode="0"+GroupePreCode;xx=GroupePreCode.toString()}
    	MessageCode += GroupePreCode
    	MessageCode += " "
      };
  return MessageCode;
  };



  Crypte.value = Encodage( Texte.value, E.value, N.value);

function Encode()
  {
  Crypte.value = Encodage( Texte.value, E.value, N.value);
  }; 



