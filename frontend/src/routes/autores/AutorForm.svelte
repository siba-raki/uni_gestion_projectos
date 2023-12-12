<script>
	import { postData } from '../../api/api';

	export let getAutores;
	export let personas;

	let biografia = '';
	let activo = false;
	let persona_id = false;

	async function submitForm() {
		try {
			await postData(`autores`, { biografia, activo, persona_id });
			getAutores();
		} catch (error) {
			console.error('Error al crear:', error);
		}
	}
</script>

<div class="bg-white text-custom-paleblue p-4">
	<form on:submit|preventDefault={submitForm} class="flex items-center justify-between">
		<div class="flex items-center space-x-4">
			<div class="flex items-center">
				<label for="biografia" class="block text-gray-700 text-sm font-bold mr-2">
					Biografia:
				</label>
				<input
					type="text"
					id="biografia"
					bind:value={biografia}
					class="shadow appearance-none border rounded w-full py-1 px-1 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
				/>
			</div>
			<div class="flex items-center">
				<label for="persona" class="block text-gray-700 text-sm font-bold mr-2"> persona: </label>
				<select
					class="border rounded w-full text-gray-700 w-full py-1 px-1 text-gray-700 leading-tight text-sm font-bold"
					bind:value={persona_id}
				>
					{#each personas as persona}
						<option value={persona.id}>{persona.nombre} {persona.apellido}</option>
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
				>Agregar</button
			>
		</div>
	</form>
</div>

<style>
	input[type='text'] {
		background-color: white;
	}
</style>
