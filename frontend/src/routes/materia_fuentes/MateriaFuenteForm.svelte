<script>
	import { postData } from '../../api/api';

	export let getMateriaFuentes;
	export let materias;
	export let fuentes;

    let materia_id = false;
    let fuente_id = false;
	let activo = true;

	async function submitForm() {
		try {
			await postData(`materia_fuentes`, { materia_id, fuente_id, activo });
			getMateriaFuentes();
		} catch (error) {
			console.error('Error al crear facultad:', error);
		}
	}
</script>

<div class="bg-white text-custom-paleblue p-4">
	<form on:submit|preventDefault={submitForm} class="flex items-center justify-between">
		<div class="flex items-center space-x-4">
			<div class="flex items-center">
				<label for="materia_id" class="block text-gray-700 text-sm font-bold mr-2"> Materia: </label>
				<select class="border rounded w-full text-gray-700 w-full py-1 px-1 text-gray-700 leading-tight text-sm font-bold" bind:value={materia_id}>
					{#each materias as materia}
						<option value={materia.id}>{materia.descripcion}</option>
					{/each}
				</select>
			</div>
            <div class="flex items-center">
				<label for="fuente_id" class="block text-gray-700 text-sm font-bold mr-2"> Fuente: </label>
				<select class="border rounded w-full text-gray-700 w-full py-1 px-1 text-gray-700 leading-tight text-sm font-bold" bind:value={fuente_id}>
					{#each fuentes as fuente}
						<option value={fuente.id}>{fuente.titulo}</option>
					{/each}
				</select>
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
				>Agregar Materia-Fuente</button
			>
		</div>
	</form>
</div>