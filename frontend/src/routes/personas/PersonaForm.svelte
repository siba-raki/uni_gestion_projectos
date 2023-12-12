<script>
	import { postData } from '../../api/api';

	export let getPersonas;
	let nombre = '';
	let apellido = '';
	let fecha_nacimiento = '';
	let activo = false;

	async function submitForm() {
		try {
			await postData(`personas`, { nombre, apellido, fecha_nacimiento, activo });
			getPersonas();
		} catch (error) {
			console.error('Error al crear Persona:', error);
		}
	}
</script>

<div class="bg-white text-custom-paleblue p-4">
	<form on:submit|preventDefault={submitForm} class="flex items-center justify-between">
		<div class="flex items-center space-x-4">
			<div class="flex items-center">
				<label for="nombre" class="block text-gray-700 text-sm font-bold mr-2"> Nombre: </label>
				<input
					type="text"
					id="nombre"
					bind:value={nombre}
					class="shadow appearance-none border rounded w-full py-1 px-1 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
				/>
			</div>
			<div class="flex items-center">
				<label for="apellido" class="block text-gray-700 text-sm font-bold mr-2"> Apellido: </label>
				<input
					type="text"
					id="apellido"
					bind:value={apellido}
					class="shadow appearance-none border rounded w-full py-1 px-1 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
				/>
			</div>
			<div class="flex items-center">
				<label for="fecha_nacimiento" class="block text-gray-700 text-sm font-bold mr-2">
					Fecha de nacimiento:
				</label>
				<input
					type="date"
					id="fecha_nacimiento"
					bind:value={fecha_nacimiento}
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
				>Agregar Persona</button
			>
		</div>
	</form>
</div>

<style>
	input[type='text'] {
		background-color: white;
	}
</style>
