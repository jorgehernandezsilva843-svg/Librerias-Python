"""
Ejemplo de uso de la librería estándar 'math'
Materia: Tópicos Avanzados de Programación
Descripción: Demuestra el uso de constantes, funciones trigonométricas,
             redondeo, logaritmos, combinatoria y operaciones matemáticas avanzadas.
"""

import math

def main():
    print("=" * 60)
    print("           EJEMPLO DE LA LIBRERÍA: MATH")
    print("=" * 60)

    # 1. Constantes matemáticas importantes
    print("\n--- 1. Constantes Matemáticas ---")
    print(f"Número Pi (math.pi):                {math.pi}")
    print(f"Número de Euler / Base e (math.e):  {math.e}")
    print(f"Número Tau (math.tau = 2*pi):       {math.tau}")
    print(f"Infinito positivo (math.inf):       {math.inf}")

    # 2. Funciones de redondeo y valor absoluto
    print("\n--- 2. Redondeo y Valor Absoluto ---")
    numero = 7.64
    print(f"Número original:                    {numero}")
    print(f"Techo / Redondeo hacia arriba (ceil):  {math.ceil(numero)}")
    print(f"Piso / Redondeo hacia abajo (floor):   {math.floor(numero)}")
    print(f"Truncar parte decimal (trunc):         {math.trunc(numero)}")
    print(f"Valor absoluto float (fabs de -15.8):  {math.fabs(-15.8)}")

    # 3. Potencias y Raíces
    print("\n--- 3. Potencias y Raíces ---")
    base = 16
    print(f"Raíz cuadrada de {base} (sqrt):        {math.sqrt(base)}")
    print(f"2 elevado a la 5 (pow):                {math.pow(2, 5)}")
    print(f"Hipotenusa de catetos 3 y 4 (hypot):   {math.hypot(3, 4)}")

    # 4. Logaritmos y Exponenciales
    print("\n--- 4. Logaritmos y Exponenciales ---")
    print(f"Logaritmo natural de e (log):          {math.log(math.e)}")
    print(f"Logaritmo base 10 de 1000 (log10):     {math.log10(1000)}")
    print(f"Logaritmo base 2 de 32 (log2):         {math.log2(32)}")
    print(f"Exponencial e^2 (exp):                 {math.exp(2)}")

    # 5. Trigonometría (conversión de grados a radianes)
    print("\n--- 5. Trigonometría ---")
    grados = 45
    radianes = math.radians(grados)
    print(f"{grados} grados en radianes:           {radianes:.4f} rad")
    print(f"Seno de {grados}° (sin):               {math.sin(radianes):.4f}")
    print(f"Coseno de {grados}° (cos):             {math.cos(radianes):.4f}")
    print(f"Tangente de {grados}° (tan):           {math.tan(radianes):.4f}")

    # 6. Combinatoria y Teoría de Números
    print("\n--- 6. Combinatoria y Teoría de Números ---")
    print(f"Factorial de 5 (factorial):            {math.factorial(5)}")
    print(f"M.C.D. de 48 y 180 (gcd):              {math.gcd(48, 180)}")
    print(f"Combinaciones de 5 elementos en 3:     {math.comb(5, 3)}")
    print(f"Permutaciones de 5 elementos en 3:     {math.perm(5, 3)}")

if __name__ == "__main__":
    main()
