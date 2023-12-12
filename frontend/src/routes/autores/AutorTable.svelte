<script>
	export let autores = [];
	export let onEdit;
	export let onDelete;
</script>

<table class="min-w-full divide-y divide-gray-200">
	<thead class="bg-custom-blue">
		<tr>
			<th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
				Id
			</th>
			<th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
				Nombre
			</th>
			<th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
				Apellido
			</th>
			<th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
				Biografia
			</th>
			<th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
				Activo
			</th>
			<th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
				Acciones
			</th>
		</tr>
	</thead>
	<tbody class="bg-white divide-y divide-gray-200">
		{#each autores as autor}
			<tr>
				<td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
					{autor.id}
				</td>
				<td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
					{autor.persona_nombre}
				</td>
				<td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
					{autor.persona_apellido}
				</td>
				<td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
					{autor.biografia}
				</td>
				<td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
					{autor.activo ? 'Sí' : 'No'}
				</td>
				<td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
					<button class="text-indigo-600 hover:text-indigo-900 mr-2" on:click={onEdit(autor)}>
						Editar
					</button>
					<button class="text-red-600 hover:text-red-900" on:click={onDelete(autor.id)}>
						Eliminar
					</button>
				</td>
			</tr>
		{/each}
	</tbody>
</table>
