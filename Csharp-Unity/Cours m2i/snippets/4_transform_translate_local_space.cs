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
        Vector3 moveVectLocal = new Vector3(0,0,1) * m_TranslationSpeed * Time.deltaTime;
        m_Transform.Translate(moveVectLocal, Space.Self);
    }
}