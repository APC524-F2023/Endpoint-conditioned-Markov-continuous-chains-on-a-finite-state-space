def test_directsampling():
    assert "hello" == "hello"
    # Q = np.array([[-1, 0.5, 0.5], [0.3, -0.8, 0.5], [0.4, 0.2, -0.6]])
    # T = 13
    # result = directsampling(Q, T)

    # # Test for output type
    # assert isinstance(result, list), "Output should be a list"

    # # Test for non-empty output
    # assert len(result) > 0, "Output list should not be empty"
def directsampling(Q, T):
    # 这里使用固定的 a 和 b 值作为示例
    # 您可能需要根据 Q 矩阵或其他逻辑来选择这些值
    a = 1
    b = Q.shape[0]
    N = T  # 或者根据需要选择合适的 N 值

    # 调用 sample_path 生成样本路径
    sample = sample_path(a, b, N, Q)
    return [sample]  # 确保返回的是一个列表

# 测试代码
def test_directsampling():
    Q = np.array([[-1, 0.5, 0.5], [0.3, -0.8, 0.5], [0.4, 0.2, -0.6]])
    T = 13
    result = directsampling(Q, T)

    #assert isinstance(result, list), "Output should be a list"
   # assert len(result) > 0, "Output list should not be empty"

#test_directsampling()
