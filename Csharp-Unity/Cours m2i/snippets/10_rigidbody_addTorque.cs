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

        // torque = couple, newton/metres
        Vector3 newAngularVelocity = hAxis * m_Transform.up * m_RotSpeed * Mathf.Deg2Rad;
        Vector3 deltaAngularVelocity = newAngularVelocity - m_Rigidbody.angularVelocity;
        m_Rigidbody.AddTorque(deltaAngularVelocity, ForceMode.VelocityChange);
    }
}