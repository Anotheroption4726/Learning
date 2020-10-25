public class MyScript : MonoBehaviour
{
    [SerializeField] private float m_TranslationSpeed;
    Transform m_Transform;

    private void Awake()
    {
        m_Transform = GetComponent<Transform>();
    }

    void Update()
    {
        // .forward = vecteur donné dans le référentiel global, shorthand for writing Vector3(0, 0, 1)
        Vector3 moveVect = transform.forward * m_TranslationSpeed * Time.deltaTime;

        //  plus performant que le simple 'transform' (m_Transform est mis en cache):
        m_Transform.position += moveVect;
    }
}