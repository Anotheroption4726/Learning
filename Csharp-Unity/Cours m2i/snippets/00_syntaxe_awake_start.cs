public class MyScript : MonoBehaviour
{
    //  Syntaxe 'PascalCase' pour paramêtres de classe
    [SerializeField] private float m_TranslationSpeed;

    //  Tooltip s'affichant en mouse over sur la variable dans l'inspector
    [Tooltip("Rotation in degrees per second")]
    [SerializeField] private float m_RotSpeed;

    Transform m_Transform;
    

    // Getters et setters (appellés propriétés en C#)
    public float GetTranslationSpeed()
    {
        return m_TranslationSpeed;
    }

    public void SetTranslationSpeed(float translationSpeed)
    {
        m_TranslationSpeed = translationSpeed;
    }


    // Initializations qui concernent que l'objet lui-même
    private void Awake()
    {
        m_Transform = GetComponent<Transform>();
    }

    //  Initializations qui concernent les objets exterieurs (s'exécute après l'execution de tous les awake appartenant à tous 
    //  les objets de la scene)
    void Start()
    {
        //  Syntaxe 'camelCase' pour variables locales
        float myVariable;
    }
}