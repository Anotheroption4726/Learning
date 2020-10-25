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
        //  quaternion d'orientation * quaternion de rotation = quaternion de nouvelle orientation
        //  !ATTENTION! Multiplication de droite à gauche
        m_Rigidbody.MoveRotation(qRot * m_Rigidbody.rotation);
    }
}