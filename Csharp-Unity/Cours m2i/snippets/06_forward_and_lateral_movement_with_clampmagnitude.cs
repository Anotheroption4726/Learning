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
        float hAxis = Input.GetAxis("Horizontal");
        float vAxis = Input.GetAxis("Vertical");

        //  Vector3 moveVect = new Vector3(hAxis, 0, vAxis) * m_TranslationSpeed * Time.deltaTime;
        //  Clamp magnitude permet de faire en sorte que la distance du vecteur ne soit pas multipliée par 2 en direction diagonale (x + y)
        Vector3 moveVect = Vector3.ClampMagnitude(new Vector3(hAxis, 0, vAxis) * m_TranslationSpeed * Time.deltaTime, 1);

        m_Transform.Translate(moveVect, Space.Self);
    }
}