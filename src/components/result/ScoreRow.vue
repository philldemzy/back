<template>
    <tr>
        <td>{{ indexOf(result) }}</td>
        <td>{{ result.student_name }}</td>
        <td>{{ result.student_id }}</td>
        <td>{{ result.score }}</td>
        <td>{{ (result.score / total) * 100 }}</td>
    </tr>
</template>

<script>
export default{
    name: 'ScoreRow',

    props: {
        result: Object,
        total: Number,
    }
}
</script>
