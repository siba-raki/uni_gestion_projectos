<script>
    import { onMount } from 'svelte';
    import { getData, deleteData } from '../../api/api';
    import MateriaTable from './MateriaTable.svelte';
    import MateriaModal from './MateriaModal.svelte';
    import MateriaForm from './MateriaForm.svelte';
    import Navbar from '../navbar/Navbar.svelte'

    let materias = [];
    let facultades = [];
    let materiaEditada = null;

    onMount(async () => {
        await getMaterias();
        await getFacultades();
    });

    async function getMaterias() {
        try {
            materias = await getData('materias/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function getFacultades() {
        try {
            facultades = await getData('facultades/');
        } catch (error) {
            console.error('Error al cargar datos:', error);
        }
    }

    async function deleteMateria(id) {
        try {
            await deleteData(`materias/${id}`);
            await getMaterias();
        } catch (error) {
            console.error('Error al eliminar materia:', error);
        }
    }

    function showModal(materia) {
        materiaEditada = materia;
    }

    function closeModal() {
        materiaEditada = null;
    }
</script>
<div>
    <Navbar />
    <MateriaForm facultades={facultades} getMaterias={getMaterias}/>
    {#if materiaEditada}
    <MateriaModal facultades={facultades} materia={materiaEditada} onClose={closeModal} getMaterias={getMaterias}/>
    {/if}
    <div class="container mx-auto w-1/2">
        <MateriaTable {materias} onEdit={showModal} onDelete={deleteMateria} />
    </div>
</div>
