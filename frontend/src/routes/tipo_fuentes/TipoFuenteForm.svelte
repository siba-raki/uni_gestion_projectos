<script>
    import { postData } from '../../api/api';

    export let getTipoFuentes;
    let descripcion = '';
    let activo = false;

    async function submitForm() {
        try {
            await postData(`tipo_fuentes`, {descripcion, activo});
			getTipoFuentes();
        } catch (error) {
            console.error('Error al crear:', error);
        }
    }
</script>

<div class="bg-white text-custom-paleblue p-4">
    <form on:submit|preventDefault={submitForm} class="flex items-center justify-between">
        <div class="flex items-center space-x-4">
            <div class="flex items-center">
                <label for="descripcion" class="block text-gray-700 text-sm font-bold mr-2">
                    Descripción:
                </label>
                <input
                    type="text"
                    id="descripcion"
                    bind:value={descripcion}
                    class="shadow appearance-none border rounded w-full py-1 px-1 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                />
            </div>
            <div class="flex items-center">
                <label for="activo" class="block text-gray-700 text-sm font-bold mr-2"> Activo: </label>
                <input
                    type="checkbox"
                    id="activo"
                    bind:checked={activo}
                    class="shadow leading-tight focus:outline-none focus:shadow-outline"
                />
            </div>
            <button type="submit" class="bg-custom-blue hover:bg-custom-lightblue text-white font-bold py-2 px-4 rounded">Agregar</button>
        </div>
    </form>
</div>

<style>
    input[type='text'] {
        background-color: white;
    }
</style>
