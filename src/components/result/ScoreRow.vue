<template>
    <tr>
        <td class="border-b border-dark1">{{ index }}</td>
        <td class="border-b border-dark1">{{ result.student_name }}</td>
        <td class="border-b border-dark1">{{ result.student_id }}</td>
        <td class="border-b border-dark1">{{ result.score }}</td>
        <td class="border-b border-dark1">{{ Math.round((result.score / total) * 100) }}%</td>
    </tr>
</template>

<script>
export default{
    name: 'ScoreRow',

    props: {
        result: Object,
        index: Number,
        total: Number,
    }
}
</script>
