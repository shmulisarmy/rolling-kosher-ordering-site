interface menuItem {
    name: string;
    price: string;
    description: string;
    image_url: string;
}

interface CartState {
    items: number[];
    total: number;
}

interface CartItemProps {
    name: string;
    price: string;
    description: string;
    image_url: string;
    index: number;
    removeFromCart: (index: number) => void;
}

interface ItemProps extends MenuItem {
    index: number;
    addToCart: (foodName: string) => void;
}

interface CartProps {
    cart: CartState;
    removeFromCart: (index: number) => void;
}