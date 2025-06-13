import streamlit as st

st.title("🛒 Lista de Compras: Perro Caliente")
st.write("Agrega productos a tu lista. Escribe los que necesites y pulsa Enter.")

# Inicializa la lista si no existe
if "lista_productos" not in st.session_state:
    st.session_state.lista_productos = []

# Agregar productos
nuevo_producto = st.text_input("Producto:")
if nuevo_producto:
    st.session_state.lista_productos.append(nuevo_producto)
    st.experimental_rerun()  # Refresca para limpiar input

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
        st.experimental_rerun()

