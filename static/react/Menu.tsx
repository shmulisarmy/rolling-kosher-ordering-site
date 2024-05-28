function Item({ name, price, description, image_url, addToCart }: ItemProps) {
    return (
        <div className="item">
            <div className="img">

                <img src={`/static/images/${name}.jpg`} alt={`${name}-image`} />
            </div>
                <div className="text">
                    <h1>{name}</h1>
                    <p>{price}</p>
                    <p>{description}</p>
                    <button onClick={() => addToCart(name)}>Add to Cart</button>
                </div>
        </div>
    )
}
const Menu = ({
  addToCart
}) => {
  return <main>
                {menu.map((item, index) => <Item key={item.name} {...item} addToCart={addToCart} />)}
            </main>;
}
  