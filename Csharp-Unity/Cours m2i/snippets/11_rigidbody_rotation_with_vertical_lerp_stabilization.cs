public class MyScript : MonoBehaviour
{
    [SerializeField] private float m_RotSpeed;
    Transform m_Transform;
    Rigidbody m_Rigidbody;

    private void Awake()
    {
        m_Transform = GetComponent<Transform>();
        m_Rigidbody = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        float hAxis = Input.GetAxis("Horizontal");

        float rotAngle = hAxis * m_RotSpeed * Time.deltaTime;
        Quaternion qRot = Quaternion.AngleAxis(rotAngle, m_Transform.up);
        Quaternion qStraightRot = Quaternion.FromToRotation(m_Transform.up, Vector3.up);
        Quaternion targetOrientation = Quaternion.Lerp(m_Rigidbody.rotation, qStraightRot * qRot * m_Rigidbody.rotation, Time.fixedDeltaTime * 4);
        m_Rigidbody.MoveRotation(targetOrientation);
    }
}