<script>
    import { updateData} from '../../api/api';

    export let fuente;
    export let onClose;
    export let getFuentes;

    async function editFuentes() {
        try {
            await updateData(`fuentes/${fuente.id}`, fuente);
            onClose();
			getFuentes();
        } catch (error) {
            console.error('Error al actualizar datos:', error);
        }
    }
</script>


<div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex justify-center items-start md:items-center pt-10 md:pt-0"
>
    <!-- Contenedor principal más ancho -->
    <div class="bg-white rounded-lg shadow overflow-hidden mx-auto p-8 w-1/2">
        <form on:submit|preventDefault={editFuentes}>
            <div class="flex flex-wrap -mx-2">
                <div class="w-full md:w-1/2 px-2 mb-4">
                    <div class="mb-4">
                        <label for="titulo" class="block text-gray-700 text-sm font-bold mb-2">
                            Titulo:
                        </label>
                        <input
                            type="text"
                            id="titulo"
                            bind:value={fuente.titulo}
                            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div class="mb-4">
                        <label for="fecha_publicacion" class="block text-gray-700 text-sm font-bold mb-2">
                            Fecha de publicación:
                        </label>
                        <input
                            type="datetime-local"
                            id="fecha_publicacion"
                            bind:value={fuente.fecha_publicacion}
                            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div class="mb-4">
                        <label for="activo" class="text-gray-700 text-sm font-bold mb-2"> Activo: </label>
                        <input
                            type="checkbox"
                            id="activo"
                            bind:checked={fuente.activo}
                            class="ml-1 shadow leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                </div>

                <div class="w-full md:w-1/2 px-2 mb-4">
                    <div class="mb-4">
                        <label for="resumen" class="block text-gray-700 text-sm font-bold mb-2">
                            Resumen:
                        </label>
                        <textarea
                        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            bind:value={fuente.resumen} />
                    </div>
                </div>

            </div>

            <div class="mt-4 flex justify-end">
                <button
                    type="button"
                    class="text-gray-600 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    on:click={onClose()}
                >
                    Cancelar
                </button>
                <button
                    type="submit"
                    class="bg-blue-500 text-white active:bg-blue-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                >
                    Guardar Cambios
                </button>
            </div>
        </form>
    </div>
</div>
