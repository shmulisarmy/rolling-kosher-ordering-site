
class ErrorBoundary extends React.Component<{}, { hasError: boolean }> {
    constructor(props: {}) {
        super(props)
        this.state = { hasError: false }
    }

    static getDerivedStateFromError() {
        return { hasError: true }
    }

    componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
        console.error(error, errorInfo)
    }

    render() {
        if (this.state.hasError) {
            return <h1 style={{ textAlign: "center", color: "red" }}>Something went wrong. please reload</h1>
        }

        return this.props.children
    }
}






function App() {
    const [cart, setCart] = React.useState(
        JSON.parse(localStorage.getItem('cart') || '{}'))

    function addToCart(foodName: string) {
      if (!(foodName in cart)) {
          cart[foodName] = 1
          localStorage.setItem('cart', JSON.stringify(cart))
          setCart({...cart})
      }

    }

    
    function removeFromCart(foodName: string) {
        delete cart[foodName]
        localStorage.setItem('cart', JSON.stringify(cart))
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
        localStorage.setItem('cart', JSON.stringify(cart))
        setCart({...cart})
    }
    function decrease(foodName: string) {
        if (cart[foodName] > 0) 
            {cart[foodName] -= 1
            localStorage.setItem('cart', JSON.stringify(cart))
            setCart({...cart})
        }
    }
    
    return (
        <div className="flex">
            <ErrorBoundary>
                <DisplayCart cart={cart} removeFromCart={removeFromCart} {...{increase, decrease}} />
            </ErrorBoundary>
            <ErrorBoundary>
                {Menu_component}
            </ErrorBoundary>
        </div>
    )
}



ReactDOM.render(<App />, document.getElementById('root'));
