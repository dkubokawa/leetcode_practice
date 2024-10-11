func removeDuplicates(nums []int) int {
    insertIdx := 1

    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            nums[insertIdx] = nums[i]
            insertIdx++
        }
    }

    return insertIdx
}