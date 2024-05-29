





function App() {
    const [cart, setCart] = React.useState(
        JSON.parse(localStorage.getItem('cart') || '{}'))

    function addToCart(foodName: string) {
      if (!(foodName in cart)) {
          cart[foodName] = 1
      }

      setCart({...cart})
    }

    
    function removeFromCart(foodName: string) {
        delete cart[foodName]
        setCart({...cart})
    }
    
    React.useEffect(
        () => {
            console.table(cart)
        },
        [cart]
    )
    
    const Menu_component = React.useMemo(() => <Menu addToCart={addToCart}  />, [])
    
    function increase(foodName: string) {
        cart[foodName] += 1
        setCart({...cart})
    }
    function decrease(foodName: string) {
        if (cart[foodName] > 0) 
            {cart[foodName] -= 1
            setCart({...cart})
        }
    }
    
    return (
        <div className="flex">

            <DisplayCart cart={cart} removeFromCart={removeFromCart} {...{increase, decrease}} />
            
            {Menu_component}
        </div>
    )
}



ReactDOM.render(<App />, document.getElementById('root'));
