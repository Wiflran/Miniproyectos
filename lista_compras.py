import streamlit as st

st.title("🛒 Lista de Compras: Perro Caliente")
st.write("Agrega productos a tu lista. Escribe los que necesites y pulsa Enter.")

# Inicializa la lista si no existe
if "lista_productos" not in st.session_state:
    st.session_state.lista_productos = []

if "nuevo_producto" not in st.session_state:
    st.session_state.nuevo_producto = ""

# Función para agregar producto
def agregar_producto():
    prod = st.session_state.nuevo_producto.strip()
    if prod:
        st.session_state.lista_productos.append(prod)
        st.session_state.nuevo_producto = ""  # Limpia el input
        st.rerun()

# Input con on_change
st.text_input("Producto:", key="nuevo_producto", on_change=agregar_producto)

# Mostrar la lista actual
if st.session_state.lista_productos:
    st.subheader("📋 Tu lista de compras:")
    for prod in st.session_state.lista_productos:
        st.write(f"• {prod}")
else:
    st.write("Aún no hay productos en la lista.")

# Eliminar productos
st.subheader("❌ ¿Deseas eliminar un producto?")
producto_a_eliminar = st.selectbox("Selecciona un producto para eliminar", options=[""] + st.session_state.lista_productos)

if producto_a_eliminar and producto_a_eliminar in st.session_state.lista_productos:
    if st.button("Eliminar producto"):
        st.session_state.lista_productos.remove(producto_a_eliminar)
        st.success(f"Producto '{producto_a_eliminar}' eliminado.")
        st.rerun()
