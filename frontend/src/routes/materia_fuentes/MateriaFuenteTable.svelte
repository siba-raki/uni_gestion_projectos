<script>
    export let materia_fuentes = [];
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
                Materia
            </th>
            <th class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                Fuente
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
        {#each materia_fuentes as materia_fuente}
            <tr>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
                    {materia_fuente.id}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
                    {materia_fuente.materia_nombre}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
                    {materia_fuente.fuente_nombre}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-custom-lightblue">
                    {materia_fuente.activo ? 'Sí' : 'No'}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                    <button
                        class="text-indigo-600 hover:text-indigo-900 mr-2"
                        on:click={onEdit(materia_fuente)}
                    >
                        Editar
                    </button>
                    <button class="text-red-600 hover:text-red-900" on:click={onDelete(materia_fuente.id)}>
                        Eliminar
                    </button>
                </td>
            </tr>
        {/each}
    </tbody>
</table>