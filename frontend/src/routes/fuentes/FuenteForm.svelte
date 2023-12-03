<script>
	import { postData } from '../../api/api';

	export let getFuentes;
	let titulo = '';
	let resumen = '';
	let fecha_publicacion = '';
	let activo = false;

	async function submitForm() {
		try {
			console.log({ titulo, resumen, fecha_publicacion, activo })
			await postData(`fuentes`, { titulo, resumen, fecha_publicacion, activo });
			getFuentes();
		} catch (error) {
			console.error('Error al crear facultad:', error);
		}
	}
</script>

<div class="bg-white text-custom-paleblue p-4">
	<form on:submit|preventDefault={submitForm} class="flex items-center justify-between">
		<div class="flex items-center space-x-4">
			<div class="flex items-center">
				<label for="titulo" class="block text-gray-700 text-sm font-bold mr-2"> titulo: </label>
				<input
					type="text"
					id="titulo"
					bind:value={titulo}
					class="shadow appearance-none border rounded w-full py-1 px-1 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
				/>
			</div>
			<div class="flex items-center">
				<label for="resumen" class="block text-gray-700 text-sm font-bold mr-2"> Resumen: </label>
				<input
					type="text"
					id="resumen"
					bind:value={resumen}
					class="shadow appearance-none border rounded w-full py-1 px-1 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
				/>
			</div>
			<div class="flex items-center">
				<label for="fecha_publicacion" class="block text-gray-700 text-sm font-bold mr-2">
					Fecha de publicación:
				</label>
				<input
					type="datetime-local"
					id="fecha_publicacion"
					bind:value={fecha_publicacion}
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
			<button
				type="submit"
				class="bg-custom-blue hover:bg-custom-lightblue text-white font-bold py-2 px-4 rounded"
				>Agregar Fuente</button
			>
		</div>
	</form>
</div>

<style>
	input[type='text'] {
		background-color: white;
	}
</style>
