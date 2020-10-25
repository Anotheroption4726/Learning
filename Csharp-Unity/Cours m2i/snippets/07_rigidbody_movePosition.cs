public class MyScript : MonoBehaviour
{
    [SerializeField] private float m_TranslationSpeed;
    Transform m_Transform;
    Rigidbody m_Rigidbody;

    private void Awake()
    {
        m_Transform = GetComponent<Transform>();
        m_Rigidbody = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        float vAxis = Input.GetAxis("Vertical");

        Vector3 moveVect = vAxis * m_Transform.forward * m_TranslationSpeed * Time.fixedDeltaTime;
        m_Rigidbody.MovePosition(m_Rigidbody.position + moveVect);
    }
}