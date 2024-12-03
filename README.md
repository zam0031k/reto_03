# Reto_03
## Clase menú:
````mermaid
classDiagram
    class MenuItem {
        +String name
        +float price
        +calculate_total(quantity: int) float
    }
````
### Atributos
* `MenuItem:`Es la clase base que representa un elemento del menú.
* `name:` El nombre del elemento del menú.
price: El precio del elemento del menú.
### Métodos:
* `calculate_total(quantity: int) -> float:` Calcula el precio total para una cantidad dada del elemento.
## Clase Beverage:
````mermaid
classDiagram
    class Beverage {
        +String size
        +String container
        +__str__() String
    }

````
* `Beverage:` Es una subclase de MenuItem que representa una bebida.
### Atributos:
* `size:` El tamaño de la bebida (por ejemplo, "500ml").
container: El tipo de contenedor de la bebida (por ejemplo, "Botella").
### Métodos:
* `__str__() -> String:` Devuelve una representación en cadena del objeto Beverage.
## Clase Appetizer
````mermaid
classDiagram
    class Appetizer {
        +String serving_size
        +String spiciness_level
        +__str__() String
    }
````
* `appertizer:` Es una subclase de MenuItem que representa un aperitivo.
### Atributos:
* `serving_sinze:` El tamaño de la porción del aperitivo (por ejemplo, "Grande").
### Métodos:
*  `__str__() -> String:` Devuelve una representación en cadena del objeto Appetizer.
## Clase MainCourse
````mermaid
classDiagram
    class MainCourse {
        +String portion_size
        +bool spiciness
        +bool sauces
        +__str__() String
    }
````
* `MainCourse:` Es una subclase de MenuItem que representa un plato principal.
### Atributos:
* `portion_size:` El tamaño de la porción del plato principal (por ejemplo, "Grande").
* `spiciness:` Indica si el plato principal es picante (True o False).
* `sauces:` Indica si el plato principal incluye salsas (True o False).
### Métodos:
* `__str__() -> String:` Devuelve una representación en cadena del objeto MainCourse.
## Clase Order
````mermaid
classDiagram
    class Order {
        +List~MenuItem~ items
        +add_item(item: MenuItem, quantity: int)
        +calculate_total() float
        +apply_discount()
        +__str__() String
    }
````
## Relación Entra clases
* `Order:` Representa una orden que contiene una lista de objetos MenuItem.
### Atributos
* `items:` Una lista de objetos MenuItem y sus cantidades.
### Métodos
* `add_item(item: MenuItem, quantity: int):` Añade un elemento a la orden.
* `calculate_total() -> float:` Calcula el monto total de la orden.
* `apply_discount():` Aplica un descuento basado en la cantidad de elementos en la orden.
* `__str__() -> String:` Devuelve una representación en cadena del objeto Order.
````mermaid
classDiagram
    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order "1" *-- "0..*" MenuItem
````
### Herencia
Beverage, Appetizer y MainCourse heredan de MenuItem.
### Composición
Order tiene una relación de composición con MenuItem, indicando que una orden puede contener múltiples elementos del menú.

## Diagrama completo
````mermaid
classDiagram
    class MenuItem {
        +String name
        +float price
        +calculate_total(quantity: int) float
    }

    class Beverage {
        +int size_ml
        +String container
        +__str__() String
    }

    class Appetizer {
        +String portion_size
        +bool sauses
        +__str__() String
    }

    class MainCourse {
        +String sinze_portion
        +bool spiciness
        +bool sauses
        +__str__() : String
    }

    class Order {
        +List items
        +add_item(item: MenuItem, quantity: int)
        +total_invoice() float
        +discount() float
        +__str__() String
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order "1..*" -- MenuItem
 
    class CocaCola {
        -size_ml = 500
        -container = "Bottle"
    }

    class OrangeJuice {
        -size_ml = 300
        -container = "Glass"
    }

    class Nachos {
        -portion_size = "Medium"
        -sauses = true
    }

    class FrenchFries {
        -portion_size = "Small"
        -sauses = false
    }

    class FruitSalad {
        -portion_size = "Medium"
        -sauses = false
    }

    class Hamburguer {
        -sinze_portion = "Medium"
        -spiciness = false
        -sauses = true
    }

    class Pizza {
        -sinze_portion = "Family"
        -spiciness = false
        -sauses = true
    }

    class Sushi {
        -sinze_portion = "Large"
        -spiciness = true
        -sauses = true
    }

    class Tacos {
        -sinze_portion = "Medium"
        -spiciness = true
        -sauses = true
    }

    Order "1..*" *-- OrangeJuice : "Orange Juice x1"
    Order "1..*" *-- Nachos : "Nachos x1"
    Order "1..*" *-- FrenchFries : "French Fries x1"
    Order "1..*" *-- FruitSalad : "Fruit Salad x1"
    Order "1..*" *-- Hamburguer : "Hamburguer x1"
    Order "1..*" *-- Pizza : "Pizza x1"
    Order "1..*" *-- CocaCola : "Coca Cola x1"
    Order "1..*" *-- Sushi : "Sushi x1"
    Order "1..*" *-- Tacos : "Tacos x1"

    Beverage <|-- CocaCola
    Beverage <|-- OrangeJuice
    Appetizer <|-- Nachos
    Appetizer <|-- FrenchFries
    Appetizer <|-- FruitSalad
    MainCourse <|-- Hamburguer
    MainCourse <|-- Pizza
    MainCourse <|-- Sushi
    MainCourse <|-- Tacos
````