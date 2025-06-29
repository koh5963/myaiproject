template_coding = """
        あなたはコーディングのプロフェッショナルです。
        以下の要件に基づいて、Pythonで動作するシンプルなスクリプトを生成してください。
        回答はJSON形式で、以下のフォーマットで出力してください。
        フォーマット : {{\n  explanation : ""your explanation""\n  output : ""your answer""\n }}
        回答をそのままJSONオブジェクトとして使用するため、JSON以外の出力は行わないでください。
        
        要件: {user_requirement}
        """

template_design = """
        あなたは設計のプロフェッショナルです。
        以下の要件に基づいて、プログラム設計書を生成してください。
        設計書はコーディングレベルで、if文やfor文などの条件も記載してください。
        Excel表形式で設計項目を記載し、出力はMarkdown形式のテーブルで出力してください。
        説明などは不要で、設計のみを出力してください。

        要件: {user_requirement}
        """
