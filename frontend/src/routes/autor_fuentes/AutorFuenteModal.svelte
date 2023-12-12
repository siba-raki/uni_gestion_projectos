<script>
	import { updateData } from '../../api/api';

	export let autor_fuente;
	export let onClose;
	export let getAutorFuentes;
	export let autores;
	export let fuentes;

	async function editAutorFuentes() {
		try {
			await updateData(`autor_fuentes/${autor_fuente.id}`, autor_fuente);
			getAutorFuentes();
			onClose();
		} catch (error) {
			console.error('Error al actualizar datos:', error);
		}
	}
</script>

<div
	class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex justify-center items-start md:items-center pt-10 md:pt-0"
>
	<div class="bg-white rounded-lg shadow overflow-hidden mx-auto p-8">
		<form on:submit|preventDefault={editAutorFuentes}>
			<div class="flex items-center space-x-4">
				<div class="flex items-center">
					<label for="autor_id" class="block text-gray-700 text-sm font-bold mr-2">
						Autor:
					</label>
					<select
						class="border rounded text-gray-700 py-2 px-3 text-gray-700 leading-tight text-sm font-bold"
						bind:value={autor_fuente.autor_id}
					>
						{#each autores as autor}
							<option value={autor.id}>{autor.persona_nombre} {autor.persona_apellido}</option>
						{/each}
					</select>
				</div>
				<div class="flex items-center">
					<label for="fuente_id" class="block text-gray-700 text-sm font-bold mr-2">
						Fuente:
					</label>
					<select
						class="border rounded text-gray-700 py-2 px-3 text-gray-700 leading-tight text-sm font-bold"
						bind:value={autor_fuente.fuente_id}
					>
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
						bind:checked={autor_fuente.activo}
						class="shadow leading-tight focus:outline-none focus:shadow-outline"
					/>
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
