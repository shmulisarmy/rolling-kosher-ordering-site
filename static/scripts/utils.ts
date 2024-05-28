function getRandomImage(): string {
    const randomImageIndex = Math.floor(Math.random() * 100);
    return `https://picsum.photos/seed/${randomImageIndex}/200`
}



function findItemByName(menu: MenuItem[], name: string): MenuItem | undefined {
    return menu.find(item => item.name === name)
}

function price_to_number(price: string): number {
    return parseFloat(price.slice(1))
}

function number_to_price(price: number): string {
    return "$" + price.toFixed(2)
}