public class MyScript : MonoBehaviour
{
    [SerializeField] private float m_TranslationSpeed;

    void Update()
    {
        // .forward = vecteur donné dans le référentiel global, shorthand for writing Vector3(0, 0, 1)

        Vector3 moveVect = transform.forward * m_TranslationSpeed * Time.deltaTime;
        transform.position += moveVect;
    }
}