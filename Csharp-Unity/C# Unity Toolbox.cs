https://docs.unity3d.com/Manual/index.html


_VARIABLE GAMEOBJECT & COMPOSANTS____________________________________

public GameObject leNom;

/*Permet de stocker un GameObject présent dans la scène dans une variable (ne pas oublier de l'"ajouter" à la variable depuis l'inspector ensuite)*/

GameObject != gameObject

/*Le gameObject (commençant par un 'g' minuscule) fait directement référence à l'objet qui porte le script. Au contraire, un GameObject (commençant par un 'G' majuscule) est une variable qui contient un objet présent dans la scène du jeu.*/




leNom.transform
//Composant de base de tout GameObject. Permet de définir la position, la rotation et la taille de l'objet passé en variable

transform.position = squarePosition;
//La position (en 2D) de l'objet qui contient le script est maintenant égale à une variable de type Vector2

transform.position.Set(0, 0, 0);
//Pas sûr de ce que ça fait mais c'est valable. (Transforme la position de l'objet par rapport à sa position courante?)

leNom.y
//Récupère une valeur égale à la position y de l'objet passé en variable

leNom.collider.bounds.size.y
/*Récupère la taille verticale du collider de l'objet passé en variable (uniquement si celui-ci possède un composant de type collider bien sûr)*/




leNom.GetComponent<>()	//Permet de manipuler directement un composant de l'objet passé en variable

GetComponent<scriptName>().functionName();
//appelle directement une fonction présente dans un script de l'objet qui contient le script

GetComponent<Renderer>().enabled = false;
//Permet de rendre "invisible" l'objet qui contient le script

leNom.GetComponent<Renderer>().material.color = Color.red;
//Permet de changer la couleur de l'objet passé en variable en rouge




leNom.SetActive(false)	//Fait disparaitre l'objet passé en variable de la scène
leNom.SetActive(true)	//Fait apparaître l'objet passé en variable dans la scène

GameObject.Find("leNom").SetActive = false;		//Fait disparaître l'objet "leNom"
GameObject.FindObjectWithTag(s)("Joueur").SetActive = false;
//Fait disparaître tous les objets possédant le tag "Joueur"




//prefabs: GameObjects déjà configurés et prêts à utiliser dans la scène (comme des templates)








_VARIABLES VECTEURS__________________________________________________

private Vector2 squarePosition;									//Vecteur en 2 dimensions
private Vector2 squarePosition = new Vector2();					//Vecteur en 2 dimensions
public Vector3Int cubePosition = new Vector3Int(0, 0, 0);		//Vecteur en 3 dimensions

squarePosition = transform.position;
squarePosition.Set(0, 0);

Vector2 squareDirection = new Vector2(1, y).normalized;			//???
Vector2 squareDirection = new Vector2(-1, y).normalized;		//???








_TILES & TILESETS____________________________________________________

using UnityEngine.Tilemaps;		//Librairie

public Tilemap tileMapName;
public Tile tileName;

tileMapName.SetTile(cubePosition, tileName);
GetComponent<Tilemap>().SetTile(cubePosition, tileName);








_SONS & MUSIQUE______________________________________________________

public AudioClip soundClip;			//Permet de stocker en variable un fichier audio
public AudioSource soundSource;		//Permet de stocker en variable un objet possédant le composant "Audio Source"

soundSource.clip = soundClip;		//Attache un AudioClip (fichier audio) à l'AudioSource (objet qui émettra le son)
soundSource.Play();					//L'AudioSource joue le son qui lui a été attaché








_PHYSIQUE ET RIGIDBODIES_____________________________________________

public float speed = 30;

GetComponent<Rigidbody2D>().velocity = Vector2.zero;
//Neutralise complètement la vitesse (en espace 2D) de l'objet qui contient le script

GetComponent<Rigidbody2D>().velocity = Vector2.right;
//L'objet qui contient le script se déplace vers la droite mais à une vitesse minimale

GetComponent<Rigidbody2D>().velocity = Vector2.left * speed;
//L'objet qui contient le script se déplace vers la gauche à une vitesse multipliée par la variable "speed"

GetComponent<Rigidbody2D>().velocity = squarePosition * speed;
//L'objet qui contient le script se déplace dans la direction de la variable "squarePosition" à une vitesse multipliée par la variable "speed"








_UI & AFFICHAGE DE TEXTE_____________________________________________

using UnityEngine.UI;				//Librairie

public int count;

public Text textName;				//Permet de stocker en variable un objet possédant le composant "Text"

textName.text = count.ToString();	//Change le texte affiché dans textName par la valeur contenue dans la variable count








_INPUTS & COMMANDES__________________________________________________

private float v;
private Vector2 squarePosition = new Vector2();
public float speed = 30;

void FixedUpdate()
{
	v = Input.GetAxisRaw("Vertical");
	//"Vertical" correspond à l'axe de type "Input" que l'on retrouve dans le menu "Edit>Project Settings>Input" de Unity
	
	squarePosition.Set(0, v);
	GetComponent<Rigidbody2D>().velocity = squarePosition * speed;
}


if (Input.GetKeyUp("space"))
{
	//Le bloc ne s'éxecute qu'une fois la barre espace du clavier pressée
}








_COROUTINES__________________________________________________________

private bool coroutineRuning = false;

    void Update()
    {
        if (coroutineRuning == false)
        {
            StartCoroutine(Everyxseconds());
        }
    }

    IEnumerator Everyxseconds()
    {
        coroutineRuning = true;
        yield return new WaitForSeconds(2);
        print(Time.time);
        coroutineRuning = false;
    }
//Affiche le temps joué toutes les 2 secondes (environ)








_FONCTIONS BUILT-IN__________________________________________________

void Awake ()
{
	//Se lit avant la fonction Start
}

void Start ()
{
	//Lue lors du démarrage, dès qu'on appuie sur play
}


void Update ()
{
	//va s'executer à chaque frame du jeu, un peu comme une boucle
}

void FixedUpdate ()
{
	//A utiliser lorsqu'on manipule des RigidBody
}

void LateUpdate ()
{
	//Appellée après la fonction Update (utile pour gérer la caméra par exemple)
}


void OnGUI ()
{
	//Ancienne fonction (peu ou plus utilisée aujourd'hui) servant à gérer l'UI
}


void OnTriggerEnter ()
{
	/*S'éxecute lorsqu'un objet entre dans la boîte de collision de l'objet qui porte le script. Chacun des deux objets nécessitant un composant de type collider (avec la case "Is Trigger" cochée).*/
}

void OnTriggerEnter (Collider col)
{
	if(col.name == "leNom")
	{
		//S'éxecute lorsque l'objet "leNom" entre dans la boîte de collision de l'objet qui porte le script.
	}
}

void OnTriggerExit ()
{
	//S'éxecute lorsqu'un objet sort de la zone de collision de l'objet qui porte le script.
}

void OnTriggerStay ()
{
	/*S'éxecute tant qu'un objet se trouve à l'intérieur de la boîte de collision de l'objet qui porte le script (comme dans une boucle).*/
}

void OnCollisionEnter2D(Collision2D col)
{
	//Différent de OnTriggerEnter? Ne marche que lorsque l'objet possède un composant "Box Collider" ou "Box Collider 2D"?

	if (col.gameObject.name == "leNom")
	{
		  //S'éxecute lorsque l'objet col correspond à l'objet s'appellant "leNom"

		  col.gameObject.GetComponent<scriptName>().functionName();
		  //appelle directement une fonction présente dans un script de l'objet col
	}
}


public GameObject objectVarName;

void OnCollisionEnter2D(Collision2D col)
{
	if (col.gameObject == objectVarName)
	{
		objectVarName.GetComponent<scriptName>().boolName = false;
		objectVarName.GetComponent<scriptName>().functionName();
	}
}








_APPEL DE FONCTIONS__________________________________________________

print();	//Affichage Console

Destroy(leNom);		//Detruit l'objet désigné
Destroy(gameObject, 3);	//Detruit l'objet qui contient le script après 3 secondes








_MISC________________________________________________________________

int nbrAleatoire;

nbrAleatoire = Random.Range(0, 2);   //nbrAleatoire est égal à un nombre aléatoire allant de 0 à 1
