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

        Vector3 newVelocity = vAxis * m_Transform.forward * m_TranslationSpeed;
        Vector3 deltaVelocity = newVelocity - m_Rigidbody.velocity;

        //  !ATTENTION! Il ne faut jamais modifier la velocity D'UN RIGIDBODY AVEC 'Rigidbody.velocity'
        //  Il faut plutôt utiliser 'Rigidbody.Addforce' avec en paramètre 'ForceMode.VelocityChange'
        m_Rigidbody.AddForce(deltaVelocity, ForceMode.VelocityChange);
    }
}