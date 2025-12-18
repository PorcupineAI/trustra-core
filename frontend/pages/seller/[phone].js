export async function getServerSideProps({ params }) {
  return { props: { phone: params.phone, score: 70 } }
}

export default function Seller({ phone, score }) {
  return (
    <div>
      <h2>Seller {phone}</h2>
      <p>Trust Score: {score}/100</p>
    </div>
  )
}
