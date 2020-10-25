public class MyScript : MonoBehaviour
{
    [SerializeField] private float m_TranslationSpeed;
    [SerializeField] private float m_RotSpeed;
    Transform m_Transform;

    private void Awake()
    {
        m_Transform = GetComponent<Transform>();
    }

    void Update()
    {
        float vAxis = Input.GetAxis("Vertical");
        Vector3 moveVectLocal = vAxis * Vector3.forward * m_TranslationSpeed * Time.deltaTime;
        m_Transform.Translate(moveVectLocal, Space.Self);

        float hAxis = Input.GetAxis("Horizontal");
        float rotAngle = hAxis * m_RotSpeed * Time.deltaTime;
        //  Vector3(0, 1, 0) == Vector3.up
        //  m_Transform.Rotate(Vector3.up, rotAngle, Space.Self);
        m_Transform.Rotate(new Vector3(0, 1, 0), rotAngle, Space.Self);
    }
}