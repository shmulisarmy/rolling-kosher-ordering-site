
function CartItem({ name, price, description, image_url, index, removeFromCart, increase, decrease, cart }: CartItemProps) {
    return (
        <div className="CartItem">

            <div className="text-and-image" style={{ display: "flex", justifyContent: "space-between" }}>
                <div className="text">

                    <h3>{name}</h3>

                    <p>{price}</p>
                    <p>quantity: {cart[name]}</p>

                    <div className="buttons">

                        <button onClick={() => removeFromCart(name)}>Remove</button>
                        <button onClick={() => decrease(index)}>-</button>
                        <button onClick={() => increase(index)}>+</button>
                    </div>
                </div>
                <img width="70px" height="70px" src={`images/${name}.jpg`} alt={`${name}-image`} style={{ padding: "4%" }} />
            </div>
        </div>
    )
}

function DisplayCart({ cart, removeFromCart, increase, decrease }: DisplayCartProps) {
    let total = 0;
    const cart_to_list = Object.keys(cart);
    return (
        <div className="cart">
            <div className="cart-icon">
                <span>&#x1F6D2;</span>
            </div>

            <div className="cartItems-container">
                {cart_to_list.length > 0 ? cart_to_list.map((key) => {
                    const price = findItemByName(menu, key).price
                    total += price_to_number(price) * cart[key]
                    return <CartItem key={key} {...findItemByName(menu, key)} index={key} removeFromCart={removeFromCart} increase={increase} decrease={decrease} cart={cart} />
                }) : <p>your cart is empty</p>}
            </div>
            <h1>Total: {number_to_price(total)}</h1>
            <button>  <span class="icon">&#x1F69A;</span>  Checkout</button>
        </div>
    )
}